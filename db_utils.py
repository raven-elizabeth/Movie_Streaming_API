from config import USER, HOST, PASSWORD
import mysql.connector
import random

# User-defined exception for error when connecting to database
class DatabaseConnectionError(Exception):
    pass


# Connect to DB
def connect_to_mysql_db(database):
    connection = mysql.connector.connect ( # Connect to MySQL using imported mysql.connector
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=database
    )
    return connection


# Open connection to database
def open_connection(name_of_db):
    my_sql_connection = connect_to_mysql_db(name_of_db)  # Connect to DB
    my_sql_cursor = my_sql_connection.cursor()  # Move cursor onto specified db
    print(f"Connected to DB: {name_of_db}")  # Evidence connection, check it worked
    return my_sql_cursor, my_sql_connection


# Close DB connection
def close_connection(connection):
    if connection:  # If function to connect to db is successful (True)...
        connection.close()  # End connection (program can finish)
        print("Terminated connection to DB")


# Function for retrieving general data
def get_all_data(query):
    db_connection = None
    try:
        cursor, db_connection = open_connection("streaming_library")
        cursor.execute(query) # Execute query
        all_data = cursor.fetchall() # Assign DB data to variable
        cursor.close() # End cursor use
        return all_data

    except Exception:
        raise DatabaseConnectionError("Unable to retrieve data from DB")

    finally:
        close_connection(db_connection)


# Find maximum ID of films in DB (same as total films in DB)
def get_max_film_id():
    get_max = "SELECT MAX(f.film_ID) FROM film f"
    return get_all_data(get_max)


# All movies
def get_all_movies():
    get_movies = "SELECT film_name FROM film ORDER BY film_ID DESC"
    return get_all_data(get_movies)


# All directors
def get_all_directors():
    get_directors = "SELECT director_forename, director_surname FROM director ORDER BY director_ID DESC"
    return get_all_data(get_directors)


# All actors
def get_all_actors():
    get_actors = "SELECT actor_forename, actor_surname FROM actor ORDER BY actor_ID DESC"
    return get_all_data(get_actors)


# All genres
def get_all_genres():
    get_genres = "SELECT genre_name FROM genre ORDER BY genre_ID DESC"
    return get_all_data(get_genres)


# All production companies
def get_all_prod_companies():
    get_prod_companies = "SELECT company_name FROM production_company ORDER BY company_ID DESC"
    return get_all_data(get_prod_companies)


# Function for retrieving filtered data
def get_filtered_data(query, filtered_search_list):
    db_connection = None
    try:
        cursor, db_connection = open_connection("streaming_library")
        cursor.execute(query, filtered_search_list)
        filtered_data = cursor.fetchall()
        cursor.close()
        return filtered_data

    except Exception:
        raise DatabaseConnectionError("Unable to retrieve data from DB")

    finally:
        close_connection(db_connection)


# Format search to appropriate MySQL format for LIKE (%)
def format_like_search(search):
    formatted_search = f"%{search.lower()}%"
    return formatted_search


# FILTERED by title
def filter_db_by_title(movie):
    get_movie = "SELECT f.film_name, f.synopsis, f.film_link FROM film f WHERE LOWER(f.film_name) LIKE %s"
    search_for_like_movie = format_like_search(movie)
    return get_filtered_data(get_movie, [search_for_like_movie])


# FILTERED by genre
def filter_db_by_genre(genre_id):
    get_genre_movies = "SELECT f.film_name, f.synopsis, f.film_link FROM film f JOIN film_genre fg ON f.film_ID = fg.film_ID WHERE fg.genre_ID = %s"
    return get_filtered_data(get_genre_movies, [genre_id])


# FILTER by director
def filter_db_by_director(first, last):
    # Used LIKE for first names in case people have multiple first names and user only searches for one
    get_director_movies = "SELECT f.film_name, f.synopsis, f.film_link FROM director d JOIN film_director fd ON d.director_ID = fd.director_ID JOIN film f ON fd.film_ID = f.film_ID WHERE LOWER(d.director_forename) LIKE %s AND LOWER(d.director_surname) = %s"
    search_for_like_first_name = format_like_search(first)
    return get_filtered_data(get_director_movies, [search_for_like_first_name, last])


# FILTER by actor
def filter_db_by_actor(first, last):
    if last == "null":  # If no last name (Zendaya)
        get_actor_movies = "SELECT f.film_name, f.synopsis, f.film_link FROM actor a JOIN film_actor fa ON a.actor_ID = fa.actor_ID JOIN film f ON fa.film_ID = f.film_ID WHERE LOWER(a.actor_forename) LIKE %s AND LOWER(a.actor_surname) IS NULL"
    else:
        get_actor_movies = "SELECT f.film_name, f.synopsis, f.film_link FROM actor a JOIN film_actor fa ON a.actor_ID = fa.actor_ID JOIN film f ON fa.film_ID = f.film_ID WHERE LOWER(a.actor_forename) LIKE %s AND LOWER(a.actor_surname) = %s"

    search_for_like_first_name = format_like_search(first)
    return get_filtered_data(get_actor_movies, [search_for_like_first_name, last])


# FILTER by production company
def filter_db_by_prod_company(prod_company):
    get_company_movies = "SELECT f.film_name, f.synopsis, f.film_link FROM production_company pc JOIN film_production_company fpc ON pc.company_ID = fpc.company_ID JOIN film f ON fpc.film_ID = f.film_ID WHERE LOWER(pc.company_name) LIKE %s"
    search_for_like_company = format_like_search(prod_company)
    return get_filtered_data(get_company_movies, [search_for_like_company])


# FILTER by user_region, choose random movie
def select_random_movie(user_region_id):
    region_filter = "SELECT f.film_name, f.synopsis, f.film_link FROM film f JOIN film_region fr ON f.film_ID = fr.film_ID JOIN region r ON fr.region_ID = r.region_ID WHERE r.region_ID = %s"
    return random.choice(get_filtered_data(region_filter, [user_region_id]))


# FILTER by film, show regions
def show_all_regions_by_film(name_of_film):
    get_regions = "SELECT r.region_ID, r.region_name FROM film f JOIN film_region fr ON f.film_ID = fr.film_ID JOIN region r ON fr.region_ID = r.region_ID WHERE LOWER(film_name) LIKE %s ORDER BY r.region_ID"
    search_for_like_films = format_like_search(name_of_film)
    return get_filtered_data(get_regions, [search_for_like_films])


# FILTER by film, find ID
def find_film_id(name_of_film):
    find_id = "SELECT film_ID FROM film WHERE LOWER(film_name) LIKE %s"
    search_for_like_films = format_like_search(name_of_film)
    return get_filtered_data(find_id, [search_for_like_films])


# Function for data that needs to be committed
def get_update_data(update_query, update_params_list, evidence_query, evidence_params_list):
    db_connection = None
    try:
        cursor, db_connection = open_connection("streaming_library")
        cursor.execute(update_query, update_params_list)
        db_connection.commit() # Commit updated changes

        if evidence_params_list is not None:
            cursor.execute(evidence_query, evidence_params_list)
        else:
            cursor.execute(evidence_query)

        evidence = cursor.fetchall()
        cursor.close()
        return evidence

    except Exception:
        raise DatabaseConnectionError("Unable to retrieve data from DB")

    finally:
        close_connection(db_connection)


# FILTER by ID, REMOVE region
def remove_film_region_by_id(film_no, region_no):
    query_to_remove = "DELETE FROM film_region WHERE film_ID = %s AND region_ID = %s"
    query_for_evidence = "SELECT r.region_name FROM film f JOIN film_region fr ON f.film_ID = fr.film_ID JOIN region r ON fr.region_ID = r.region_ID WHERE f.film_ID = %s"
    return get_update_data(query_to_remove, [film_no, region_no], query_for_evidence, [film_no])


# FILTER by ID, find title to display to user
def get_id_title(id_of_film):
    get_title = "SELECT f.film_name FROM film f WHERE f.film_ID = %s" # Avoid using f strings as they are not secure!
    return get_filtered_data(get_title, [id_of_film])


# FILTER by ID, add region
def add_film_region_by_id(id_of_film, id_of_region):
    query_to_add = "INSERT INTO film_region (film_ID, region_ID) VALUES (%s, %s)"
    query_for_evidence = "SELECT r.region_name FROM film f JOIN film_region fr ON f.film_ID = fr.film_ID JOIN region r ON fr.region_ID = r.region_ID WHERE f.film_ID = %s"
    return get_update_data(query_to_add, [id_of_film, id_of_region], query_for_evidence, [id_of_film])


# Add new film with stored proc and user dictionary
def add_new_film(data_dict):
    db_connection = None
    try:
        cursor, db_connection = open_connection("streaming_library")
        cursor.callproc("add_new_film", [data_dict["film"], data_dict["synopsis"], data_dict["link"]])
        db_connection.commit()

        evidence = get_all_movies()
        cursor.close()
        return evidence

    except Exception:
        raise DatabaseConnectionError("Unable to retrieve data from DB")

    finally:
        close_connection(db_connection)


# Functions for adding film_genre entry
# MySQL SELECT statement to find genre_ID that matches with genre_name
def get_genre_id(genre_name):
    find_id = "SELECT genre_ID FROM genre WHERE genre_name = %s"
    return get_filtered_data(find_id, [genre_name])


# Insert new genre, return list of genres for evidence of insert
def add_new_genre(new_genre):
    query_to_insert = "INSERT INTO genre (genre_name) VALUES (%s)"
    query_for_evidence = "SELECT genre_name FROM genre ORDER BY genre_ID DESC"
    return get_update_data(query_to_insert, [new_genre], query_for_evidence, None)


# Get all film_ID/genre_ID entries from film_genre and return response (can prevent duplicate errors)
def get_film_genre(film_no):
    show_all_film_genres = "SELECT film_ID, genre_ID FROM film_genre WHERE film_ID = %s"
    response = get_filtered_data(show_all_film_genres, [film_no])
    return response


# Checks if genre already exists, returns 0 if not, ID of genre if it does exist
def check_if_genre_exists(existing_list, name_of_genre):
    check_for_current_id = 0
    for genre in existing_list:
        if genre[0].lower() == name_of_genre.lower():  # existing_list returns list of tuples including comma, so [0] gets just the genre_name
            check_for_current_id = existing_list.index(genre) + 1  # Should give the genre ID (will be above 0)
    return check_for_current_id


# Collect functions to add a genre to a film
def add_film_genre(film_num, name_of_genre):

    # Find genre_ID
    all_genres = get_all_genres()
    genre_num = check_if_genre_exists(all_genres, name_of_genre)

    # If genre does not exist in DB, add genre to DB and find new ID
    if genre_num == 0:
        add_new_genre(name_of_genre)
        find_new_id = get_genre_id(name_of_genre)
        genre_num = find_new_id[0][0] # find_new_id returns a tuple within a list so [0][0] actually gets to the ID number

    # If film/region not already exists, insert
    all_film_genres = get_film_genre(film_num)
    if (film_num, genre_num) not in all_film_genres:
        query_to_insert = "INSERT INTO film_genre (film_ID, genre_ID) VALUES (%s, %s)"
        query_for_evidence = "SELECT g.genre_name FROM film f JOIN film_genre fg ON f.film_ID = fg.film_ID JOIN genre g ON fg.genre_ID = g.genre_ID WHERE f.film_ID = %s"
        response = get_update_data(query_to_insert, [film_num, genre_num], query_for_evidence, [film_num])
        return response
    else:
        return f"Film of ID: {film_num} already has '{name_of_genre}' genre"


# Function for adding bug reports to separate SQL DB
def add_user_bug_report(user_report):
    db_connection = None
    try:
        cursor, db_connection = open_connection("user_error_reports")
        add_report = "INSERT INTO error_reports (user_message) VALUES (%s)"
        cursor.execute(add_report, [user_report])
        db_connection.commit()

        evidence_report = "SELECT user_message, date_registered FROM error_reports ORDER BY date_registered DESC"
        cursor.execute(evidence_report)
        evidence = cursor.fetchall()
        cursor.close()
        return evidence

    except Exception:
        raise DatabaseConnectionError("Unable to retrieve data from DB")

    finally:
        close_connection(db_connection)


# Main program that calls functions
def main():
    # This is where I tested my functions, if you want an example, uncomment the print statement below
    #print(add_film_genre(1, "Magical"))
    pass

# Dunder main (main guard)
if __name__ == "__main__": # If active agent activates the script, run program
    main()