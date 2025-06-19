# Imports
from flask import Flask, jsonify, request
from db_utils import (get_all_movies, filter_db_by_genre, filter_db_by_title, filter_db_by_director,
                      filter_db_by_actor, get_all_directors, get_all_actors, get_all_genres,
                      get_all_prod_companies, filter_db_by_prod_company, find_film_id, show_all_regions_by_film,
                      remove_film_region_by_id, add_film_region_by_id, select_random_movie, get_max_film_id,
                      get_id_title, add_new_film, add_film_genre, add_user_bug_report)

app = Flask(__name__) # Creates flask app

# General GET endpoints

# Find total number of films in DB
@app.route("/movies/id/max", methods=["GET"])
def find_max_id():
    return jsonify(get_max_film_id())


# Random movie choice
@app.route("/movies/region/<int:region_id>/random", methods=["GET"])
def get_random_movie(region_id):
    return jsonify(select_random_movie(region_id))


# Endpoint to find film_ID
@app.route("/movies/<string:title>/id", methods=["GET"])
def search_movie_title_for_id(title):
    response = find_film_id(title)
    return jsonify(response)


# Endpoint to show all regions where film is available
@app.route("/movies/<string:title>/regions", methods=["GET"])
def show_available_regions(title):
    response = show_all_regions_by_film(title)
    return jsonify(response)


# GET: See all...
# All movies
@app.route("/movies", methods=["GET"])
def show_all_movies():
    return jsonify(get_all_movies())


# All directors
@app.route("/directors", methods=["GET"])
def see_all_directors():
    return jsonify(get_all_directors())


# All actors
@app.route("/actors", methods=["GET"])
def see_all_actors():
    return jsonify(get_all_actors())


# All genres
@app.route("/genres", methods=["GET"])
def see_all_genres():
    return jsonify(get_all_genres())


# All prod companies
@app.route("/production_company", methods=["GET"])
def see_all_prod_companies():
    return jsonify(get_all_prod_companies())


# GET method: Filter by...
# Specified movie title
@app.route("/movies/<string:title>", methods=["GET"])
def search_by_title(title):
    return jsonify(filter_db_by_title(title))


# Movies of specified genre
@app.route("/movies/genres/<int:genre_no>", methods=["GET"])
def search_by_genre(genre_no):
    return jsonify(filter_db_by_genre(genre_no))


# Movies by specified director
@app.route("/movies/directors/<string:director_firstname>-<string:director_lastname>", methods=["GET"]) # Use - to tell flask there are separate search terms
def search_by_director(director_firstname, director_lastname):
    response = filter_db_by_director(director_firstname, director_lastname)
    return jsonify(response)


# Movies featuring specified actor
@app.route("/movies/actors/<string:actor_firstname>-<string:actor_lastname>", methods=["GET"]) # Use - to tell flask there are separate search terms
def search_by_actor(actor_firstname, actor_lastname):
    response = filter_db_by_actor(actor_firstname, actor_lastname)
    return jsonify(response)


# Movies made by specified production company
@app.route("/movies/production_company/<string:company>", methods=["GET"])
def search_by_prod_company(company):
    response = filter_db_by_prod_company(company)
    return jsonify(response)


# Find film title by searching for film ID
@app.route("/movies/id/<int:movie_id>", methods=["GET"])
def search_title_by_id(movie_id):
    response = get_id_title(movie_id)
    return jsonify(response)


# POST endpoint to add available regions for film
@app.route("/movies/<int:film_id>/availability/add/<int:region_id>", methods=["POST"])
def add_region_for_film(film_id, region_id):
    response = add_film_region_by_id(film_id, region_id)
    return jsonify(response)


# Add new film
@app.route("/movies/add", methods=["POST"])
def add_new_film_to_db():
    film_dict = request.get_json()
    return jsonify(add_new_film(film_dict))


# Add genre for film
@app.route("/movies/<int:film_id>/add/genre/<string:genre_name>", methods=["POST"])
def add_genre_for_film(film_id, genre_name):
    response = add_film_genre(film_id, genre_name)
    return jsonify(response)


# Additional endpoint: DELETE endpoint to remove available regions for film
@app.route("/movies/<int:film_id>/availability/delete/<int:region_id>", methods=["DELETE"])
def remove_region_for_film(film_id, region_id):
    response = remove_film_region_by_id(film_id, region_id)
    return jsonify(response)


# Optional add bug report via separate database
@app.route("/bug_report", methods=["POST"])
def add_error_report():
    user_error_report = request.get_json()
    response = add_user_bug_report(user_error_report)
    return jsonify(response)


# Dunder main
if __name__ == "__main__":
    app.run()