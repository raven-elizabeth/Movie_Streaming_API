# Client side here

import requests
import webbrowser
import json


# Using requests to get endpoint data and convert to json
def json_get_endpoint(endpoint):
    return requests.get(endpoint).json()


def json_delete_endpoint(endpoint):
    return requests.delete(endpoint).json()


def json_post_endpoint(endpoint):
    return requests.post(endpoint).json()


# Show data functions
def get_user_data_choice():
    show_data_options = "Show all:\n    *1* Movies\n    *2* Directors\n    *3* Actors\n    *4* Genres\n    *5* Production Companies\n"
    user_data_choice = validate_int_input(show_data_options, 6)
    return user_data_choice


def show_data():
    show_all_data = get_user_data_choice()
    if show_all_data == 1:
        return see_all_movies()
    elif show_all_data == 2:
        return see_all_directors()
    elif show_all_data == 3:
        return see_all_actors()
    elif show_all_data == 4:
        return see_all_genres()
    else:
        return see_all_prod_companies()


# ALL movies
def see_all_movies():
    return json_get_endpoint("http://127.0.0.1:5000/movies")


# ALL directors
def see_all_directors():
    return json_get_endpoint("http://127.0.0.1:5000/directors")


# ALL actors
def see_all_actors():
    return json_get_endpoint("http://127.0.0.1:5000/actors")


# ALL genres
def see_all_genres():
    return json_get_endpoint("http://127.0.0.1:5000/genres")


# ALL production companies
def see_all_prod_companies():
    return json_get_endpoint("http://127.0.0.1:5000/production_company")


# Get user's intention for using the program
def get_user_intention():
    user_intention = None
    invalid_intention = 1
    print("Would you like to:")
    while invalid_intention > 0:
        user_intention = input("a) Watch a movie\nb) Edit the catalogue\nc) Show data from DB\nd) Submit bug report\n").lower()
        if user_intention == "a" or user_intention == "a)" or user_intention == "b" or user_intention == "b)" or user_intention == "c" or user_intention == "c)" or user_intention == "d" or user_intention == "d)" or user_intention[0:5] == "watch" or user_intention[0:4] == "edit" or user_intention[0:4] == "show" or user_intention[0:6] == "submit":
            invalid_intention -= 1
            if user_intention == "a" or user_intention == "a)" or user_intention[0:5] == "watch":
                user_intention = "watch"
            elif user_intention == "b" or user_intention == "b)" or user_intention[0:4] == "edit":
                user_intention = "edit"
            elif user_intention == "c" or user_intention == "c)" or user_intention[0:4] == "show":
                user_intention = "show"
            else:
                user_intention = "bug"
        else:
            print("You must choose a valid option")
    return user_intention


# Function to validate user integer input
def validate_int_input(message, more_than_valid_int):
    user_response = None
    invalid_response = 1
    while invalid_response > 0:
        try:
            user_response = int(input(message))
            if 0 < user_response < more_than_valid_int:
                invalid_response -= 1
            else:
                raise ValueError
        except ValueError:
            print("You must enter a valid integer response.")
    return user_response


# Function to validate user string input (used where appropriate)
def validate_str_input(message):
    user_response = None
    invalid_response = 1
    while invalid_response > 0:
        try:
            user_response = input(message)
            if 2 < len(user_response) and not user_response.isspace(): # If length of user response is greater than 2 and not only spaces
                invalid_response -= 1
            else:
                raise ValueError
        except ValueError:
            print("You must enter a valid response that is greater than two characters and not empty.")
    return user_response


# Watch movie functions:

# Get user region
def get_user_region():
    print("Choose a region: (Enter the corresponding number)")
    region_options = "1. Europe 2. Africa 3. North America 4. South America 5. Oceania 6. Asia \n"
    user_region = validate_int_input(region_options, 7)
    return user_region


# User chooses to search by name/genre/director/actor/production company/random
def get_user_search_choice():
    print("How would you like to search for a film? Search by:")
    search_options = "   *1* NAME\n   *2* GENRE\n   *3* DIRECTOR\n   *4* ACTOR\n   *5* PRODUCTION COMPANY\n   *6* CHOOSE FOR ME\n"
    user_search_choice = validate_int_input(search_options, 7)
    return user_search_choice


# User chooses if they want to 'watch' the movie
def get_user_play_choice():
    print("\n*** Beware: answering 'y' or 'yes' to the following will result in the opening of a YouTube link in a new page ***\n")
    while True:
        video_choice = input("Play movie? (y/n) ").lower()
        if video_choice == "y" or video_choice[0:3] == "yes":
            return True
        elif video_choice == "n" or video_choice[0:3] == "no":
            return False


# Function to simulate 'play' button
def play_movie(youtube_video):
    if get_user_play_choice(): # Simulate a 'play' button
        webbrowser.open(youtube_video) # The movie could begin playing here, but of course I don't actually have the files for that, so I've used webbrowser to open a link to a YouTube trailer for the movie instead


# Filtered search functions:

# Show user what they searched for
def display_user_search(search):
    try:
        print(f"You have selected: {search[0].title()} {search[1].title()}")
    except IndexError: # E.g. only one name (Zendaya)
        print(f"You have selected: {search[0].title()}")
        search.append("null")
    except AttributeError: # E.g. for ID searches with integers (genre search)
        print(f"You have selected: {search}")


# Reusable searching/loading messages
def search_messages(search_method):
    if search_method == "title":
        message_1 = f"Searching for movie with this title..."
    else:
        message_1 = f"Searching for {search_method} with this name..."
    message_2 = f"Loading movies associated with this {search_method}..."
    message_3 = f"No movies found for this {search_method}"
    return message_1, message_2, message_3


# Film/region endpoint
def get_film_region(movie_name):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/{movie_name}/regions")


# Get user region, determine if they can watch film in their region
def verify_user_film_region(film):
    print("Which region are you in? ")
    user_region = get_user_region()
    film_regions = get_film_region(film)
    for region_data in film_regions:
        for region_detail in region_data:
            if region_detail == user_region:
                return True
    return False


# Display results of chosen movie
def display_movie_details(result, index):
    movie_title = result[index][0]
    print(f"Movie: {movie_title}")
    print(f"Movie synopsis: {result[index][1]}")

    if verify_user_film_region(movie_title):
        play_movie(result[index][2])
    else:
        print("This movie is currently unavailable in your region.")


# User can choose if more than one movie option
def get_user_film_choice(len_of_movie_options):
    user_film_choice = "Enter the number of the film you would like to watch: "
    validate_choice = validate_int_input(user_film_choice, len_of_movie_options + 1)
    return validate_choice


# For requests resulting in multiple movie options, display each option
def cycle_through_movies(request_response, message):
    request_length = len(request_response)
    if request_length == 0:
        print(message)
    elif request_length == 1:
        display_movie_details(request_response, 0)
    else:
        for movie in request_response:
            print(f"{request_response.index(movie) + 1}. {movie[0]}")
        film_choice = get_user_film_choice(request_length)
        display_movie_details(request_response, (film_choice - 1))


# Function that brings together multiple movie result functions
def display_search_process(user_search, filter_method, filtered_result):
    display_user_search([user_search])

    searching_message, loading_message, none_message = search_messages(filter_method)
    print(searching_message)
    print(loading_message)

    cycle_through_movies(filtered_result, none_message)


# Search by title
# Filter by title endpoint
def title_search(title):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/{title}")


# Get user to enter movie title
def get_user_title():
    instructions = "Enter the title of the movie you are searching for: "
    user_title = validate_str_input(instructions)
    return user_title


# Function to collect all title search functions
def search_for_title():
    searched_title = get_user_title()
    title_result = title_search(searched_title)
    display_search_process(searched_title, "title", title_result)


# Search by genre
# Filter by genre endpoint
def genre_search(genre_num):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/genres/{genre_num}")


# Get user genre
def get_user_genre():
    print("What genre will you search for?")
    genre_options = see_all_genres()
    count = len(genre_options)
    for genre in genre_options:
        print(f"    {count}. {genre[0].upper()}")
        count -= 1
    genre_prompt = "Enter the corresponding number of the genre you wish to choose: "
    user_genre = validate_int_input(genre_prompt, len(genre_options) + 1)
    return user_genre


# Collect genre search functions
def search_for_genre():
    searched_genre = get_user_genre()
    genre_result = genre_search(searched_genre)
    display_search_process(searched_genre, "genre", genre_result)


# Search by director
# Filter by director endpoint
def director_search(first_name, last_name):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/directors/{first_name}-{last_name}")


# Get user director
def get_user_director():
    instructions = "Search for a director: "
    user_director = validate_str_input(instructions)
    director_names = user_director.lower().split()
    return director_names


# Collect director search functions
def search_for_director():
    searched_director = get_user_director()
    try:
        director_result = director_search(searched_director[0], searched_director[1])
        display_search_process(searched_director, "director", director_result)
    except IndexError:
        print("You must search with a first and last name")
        search_for_director()


# Search by actor
# Filter by actor endpoint
def actor_search(first_name, last_name):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/actors/{first_name}-{last_name}")


# Get user actor
def get_user_actor():
    instructions = "Search for an actor: "
    user_actor = validate_str_input(instructions)
    actor_names = user_actor.lower().split()
    return actor_names


# Collect actor search functions
def search_for_actor():
    try:
        searched_actor = get_user_actor()
        actor_result = actor_search(searched_actor[0], searched_actor[1])
        display_search_process(searched_actor, "actor", actor_result)
    except IndexError:
        print("You must search with a first and last name")
        search_for_actor()


# Search by production company
# Filter by production company endpoint
def prod_company_search(company_name):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/production_company/{company_name}")


# Get user production company
def get_user_prod_company():
    instructions = "Search for a production company: "
    user_prod_company = validate_str_input(instructions)
    return user_prod_company


# Collect production company search functions
def search_for_prod_company():
    searched_prod_company = get_user_prod_company()
    prod_company_result = prod_company_search(searched_prod_company)
    display_search_process(searched_prod_company, "production company", prod_company_result)


# Search randomly
# Endpoint filtered by region
def random_movie_search():
    user_region = get_user_region()
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/region/{user_region}/random")


# Random choice of region-available movies
def choose_random_movie(response):
    print(f"Random choice loading...")
    if len(response) == 0:
        print("Error: Unable to find any movies in the DB that are available in your region")
    else:
        print(f"Movie: {response[0]}")
        print(f"Movie synopsis: {response[1]}")
        play_movie(response[2])


# Options for watching movie
def watch_movie():
    search_method = get_user_search_choice()
    if search_method == 1:
        search_for_title()

    elif search_method == 2:
        search_for_genre()

    elif search_method == 3:
        search_for_director()

    elif search_method == 4:
        search_for_actor()

    elif search_method == 5:
        search_for_prod_company()

    else: # Random selection
        choose_random_movie(random_movie_search())


# Edit option functions
# User edit choice
def get_user_edit_choice():
    print("Choose an option:")
    edit_options = "    *1* Update region availability\n    *2* Add new data\n"
    user_edit_choice = validate_int_input(edit_options, 3)
    return user_edit_choice


# User choice for region availability
def get_user_region_choice():
    region_options = "\n1. Add region availability\n2. Remove region availability\n3. Show all available regions for film \n4. Retrieve movie ID\n"
    user_region_choice = validate_int_input(region_options, 5)
    return user_region_choice


# Find ID of a movie
# Filter by ID endpoint
def get_film_id(movie_name):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/{movie_name}/id")


# Prevent errors if more than one ID is returned
def display_multiple_id(response):
    print("More than one ID has been found due to entries with similar names\nThe ID you are looking for could be: ")
    for i in response:
        print(i)
    print("Please consult the DB manually to ensure you choose the right ID")


# Collect find ID functions and prevent errors for non-existent data
def find_film_id():
    retrieved_id = get_film_id(get_user_title())
    if len(retrieved_id) == 0:
        print("This film does not appear to exist in the DB")
    elif len(retrieved_id) > 1:
        display_multiple_id(retrieved_id)
    else:
        id_num = retrieved_id[0][0]
        print(f"This is the ID found for your search: {id_num}")


# Show all regions where film is available
def show_film_region():
    available_regions = get_film_region(get_user_title())
    if len(available_regions) > 0:
        print("Regions where this film is available: (ID. Region)")
        for region in available_regions:
            print(f"{region[0]}. {region[1]}")
    else:
        print("This film has no associated regions within the DB.")


# Add new region where film is available
# Add film/region endpoint
def add_film_region_endpoint(movie_id, region_id):
    return json_post_endpoint(f"http://127.0.0.1:5000/movies/{movie_id}/availability/add/{region_id}")


# Find max possible ID of move in DB to prevent user searching for non-existent data
def fetch_max_film_id():
    endpoint = json_get_endpoint("http://127.0.0.1:5000/movies/id/max")
    return endpoint


# Get film ID from user
def get_user_film_id():
    instructions = "Enter ID of the film: "
    exceeds_max_film_id = fetch_max_film_id()[0][0] + 1
    film_num = validate_int_input(instructions, exceeds_max_film_id)
    return film_num


# Filter by ID endpoint to return title of film to user
def find_title_by_id(user_id):
    return json_get_endpoint(f"http://127.0.0.1:5000/movies/id/{user_id}")


# Get user input on updating region (reusable for add/remove)
def choose_region_to_update(update_method, possible_update_regions):
    print(f"Which region would you like to make this film {update_method} in? (Enter the corresponding number)")  # If film has at least one region where it is not available...
    which_region = ""
    for region in possible_update_regions:
        which_region = which_region + f"{region[0]}. {region[1]}\n"
    region_num = validate_int_input(which_region, len(which_region) + 1)
    return region_num


# Return possible regions for film to be added to
def get_available_add_regions(prior_regions_list):
    region_options = [[1, 'Europe'], [2, 'Africa'], [3, 'North America'], [4, 'South America'], [5, 'Oceania'], [6, 'Asia']]
    for prior_region in prior_regions_list:
        if prior_region in region_options:
            region_options.remove(prior_region)

    return region_options


# Function to prevent errors where film already has full availability
def attempt_region_add(region_list, film_no):
    if len(region_list) > 0:
        user_region = choose_region_to_update("available", region_list)
        additional_availability = add_film_region_endpoint(film_no, user_region)
        print("Movie is now available in chosen region")
        return additional_availability

    else:
        return None


# Show which film the user is updating regions for
def display_found_movie_by_id():
    film_id = get_user_film_id()
    found_film = find_title_by_id(film_id)[0][0]
    print(f"Movie found: {found_film}")
    return found_film, film_id


# Collect functions for adding a film/region
def add_film_region():
    user_film, user_film_id = display_found_movie_by_id()
    current_regions = get_film_region(user_film)
    available_add_regions = get_available_add_regions(current_regions)
    return attempt_region_add(available_add_regions, user_film_id)


# Remove region where film is available
# Delete film/region endpoint
def delete_film_region_endpoint(movie_id, region_id):
    endpoint = json_delete_endpoint(f"http://127.0.0.1:5000/movies/{movie_id}/availability/delete/{region_id}")
    return endpoint


# Get user to choose to remove from regions where the film is currently available
def remove_film_region():
    film, film_no = display_found_movie_by_id()
    current_regions = get_film_region(film)
    if len(current_regions) > 0:
        region_no = choose_region_to_update("unavailable", current_regions)
        removed_availability = delete_film_region_endpoint(film_no, region_no)
        print(f"{film} is no longer available in region of ID: {region_no}")
        return removed_availability
    else:
        return None


# Function to display outcome for updating film/region
def display_updated_regions(update_response, update_method):
    if update_response is None:
        availability = "available"
        if update_method == "remove":
            availability = "un" + availability
        print(f"This movie is already {availability} in all regions - nothing to {update_method}")
    else:
        print("Regions where film is available:")
        for response in update_response:
            print(f"    * {response[0]}")


# ADD NEW FILM WITH REQUESTS & DICTIONARY
# Add film endpoint with headers and json.dumps dictionary
def add_film_to_db(film_dict):
    endpoint = "http://127.0.0.1:5000/movies/add"
    response = requests.post(endpoint, headers={'content-type': 'application/json'}, data=json.dumps(film_dict))
    return response.json()


# Get user details for new film dictionary
def get_user_dict():
    title_message = "Enter the title of the new movie: "
    synopsis_message = "Enter the synopsis of the new movie: "
    link_message = "Enter the youtube link for the movie's trailer: "
    title = validate_str_input(title_message)
    synopsis = validate_str_input(synopsis_message)
    link = validate_str_input(link_message)
    return title, synopsis, link


# Get user choice on adding movie or movie genre
def get_add_data_option():
    print("What would you like to add?")
    options = "     *1* MOVIE\n     *2* MOVIE GENRE\n"
    user_choice = validate_int_input(options, 3)
    return user_choice


# Collect functions for adding new film and present results
def add_new_film():
    film, summary, video = get_user_dict()
    user_dict = {
        "film": film,
        "synopsis": summary,
        "link": video
    }
    response = add_film_to_db(user_dict)
    print("Movies in DB: ")
    for i in response:
        print(i[0])


# Get user genre addition
def get_user_film_genre_to_add():
    film_no = get_user_film_id()
    genre_addition = "Which genre would you like to add? "
    genre = validate_str_input(genre_addition)
    return film_no, genre


# Return json data from endpoint to add genre for film
def add_genre_for_film(film_num, genre_str):
    endpoint = json_post_endpoint(f"http://127.0.0.1:5000/movies/{film_num}/add/genre/{genre_str}")
    return endpoint


# Verify yes response to a yes/no question
def user_yes_response(message):
    user_input = input(message).lower()
    if user_input == "y" or user_input[0:3] == "yes":
        return True
    else:
        return False


# Collect functions for adding genre to film and present results
def add_film_genre():
    try:
        film_id, genre_name = get_user_film_genre_to_add()
        updated_film_genres =  add_genre_for_film(film_id, genre_name)
        print(f"{genre_name} genre added for film of ID: {film_id}")
        print("All genres for this film: ")
        for i in updated_film_genres:
            print(i[0])
    except requests.exceptions.JSONDecodeError:
        print("Please ensure that you are not adding a genre that this film is already associated with.")
        print("If this is not the case, please report the issue")
        if user_yes_response("Would you like to report a bug? (y/n)"):
            bug_report()


# Edit options
def edit_db():
    user_choice = get_user_edit_choice()
    if user_choice == 1:
        region_update_choice = get_user_region_choice()
        if region_update_choice == 1:
            display_updated_regions(add_film_region(), "add")
        elif region_update_choice == 2:
            display_updated_regions(remove_film_region(), "remove")
        elif region_update_choice == 3:
            show_film_region()
        else:
            find_film_id()
    else: # Add new data
        add_option = get_add_data_option()
        if add_option == 1:
            add_new_film()
        else : # Option 2: Add film/genre
            add_film_genre()


# Get user input on their bug
def get_user_bug_report():
    validate_length = 256
    validate_not_empty_response = None
    while validate_length > 255:
        bug_message = "Please describe the bug. Any error message/code, why you think it is happening, when/where it is happening (limit 255 char) "
        validate_not_empty_response = validate_str_input(bug_message)
        validate_length = len(bug_message)
    return validate_not_empty_response


# Access bug report endpoint and return response
def bug_report_endpoint(user_bug_report):
    endpoint = "http://127.0.0.1:5000/bug_report"
    response = requests.post(endpoint, headers={'content-type': 'application/json'}, data=json.dumps(user_bug_report))
    return response.json()


# Collect functions for report bugs and display feedback
def bug_report():
    if user_yes_response("Would you like to report a bug? (y/n) "):
        user_report = get_user_bug_report()
        all_reports = bug_report_endpoint(user_report)
        print("Added your bug report to the user_error_reports DB")
        print("All reports:")
        for report in all_reports:
            print(f"Report added: {report[1]}\nReport message: {report[0]}\n")
    else:
        print("No report added")


# Main program
def choose_option():
    option = get_user_intention()
    if option == "watch":
        watch_movie()
    elif option == "show":
        show_all = show_data()
        for data in show_all:  # For separate response items... (e.g. movie, director full name)
            for i in data:  # For item in each separate response... (e.g. first name, last name)
                if i is not None:  # Where data is not NULL
                    print(i, end=" ")  # print item followed by a space and then second item (shows full first name on one line)
            print("")  # New line for separate response items (e.g. separate directors/movies)
    elif option == "edit":
        edit_db()
    else: # Report bugs
        bug_report()


# Main run function
def run():
    print("\n--------- Welcome to Raven's Streaming Service ---------\n")

    counter = 0
    while counter == 0: # Continuous use of program until user actively exits
        choose_option()
        if user_yes_response("Exit program? (y/n) "):
            counter = 1

    print("\n----- Thank you for using Raven's Streaming Services -----")


# Dunder main / main guard
if __name__ == "__main__":
    run()


# If I had more time, I would include functionality for adding/removing actors, directors, production companies and for removing films
# I would also have included time delays so that the print statements don't all appear at once!
# I believe it may be better to use headers/data for all endpoints too