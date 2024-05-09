import streamlit as st

st.title("Movie Recommender System")

movies = {
    "Inception": {
        "Genres": ["Action", "Sci-Fi"],
        "Year": 2010,
        "Run Time": 148,
        "Rating": 8.8,
        "Actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]
    },
    "Interstellar": {
        "Genres": ["Adventure", "Drama", "Sci-Fi"],
        "Year": 2014,
        "Run Time": 169,
        "Rating": 8.6,
        "Actors": ["Matthew McConaughey", "Anne Hathaway"]
    },
    "The Dark Knight": {
        "Genres": ["Action", "Crime", "Drama"],
        "Year": 2008,
        "Run Time": 152,
        "Rating": 9.0,
        "Actors": ["Christian Bale", "Heath Ledger"]
    },
    "Forrest Gump": {
        "Genres": ["Drama", "Romance"],
        "Year": 1994,
        "Run Time": 142,
        "Rating": 8.8,
        "Actors": ["Tom Hanks", "Robin Wright"]
    },
    # Add more movies as per your initial dictionary
}

def recommend_movies(genre):
    recommended = [title for title, details in movies.items() if genre in details["Genres"]]
    if recommended:
        return f"Based on your love for {genre}: {', '.join(recommended)}"
    else:
        return "No movies found for this genre. Try again."

def find_movie(movie_name):
    for title, details in movies.items():
        if movie_name.lower() in title.lower():
            return f"Movie Found: {title}\nDetails: Year: {details['Year']}\nRun Time: {details['Run Time']} minutes\nRating: {details['Rating']}\nActors: {', '.join(details['Actors'])}\n"
    return "Movie not found. Please try another title."

def add_movie(name, genres, year, run_time, rating, actors):
    if name not in movies:
        movies[name] = {"Genres": genres, "Year": year, "Run Time": run_time, "Rating": rating, "Actors": actors}
        return f"Movie '{name}' added successfully!"
    else:
        return "Movie already exists."

st.sidebar.title("Actions")
action = st.sidebar.radio("Choose an action:", ["Recommend Movies", "Find a Movie", "Add a Movie"])

if action == "Recommend Movies":
    genre = st.sidebar.text_input("Enter your favorite genre:")
    if st.sidebar.button("Recommend"):
        results = recommend_movies(genre)
        st.write(results)

elif action == "Find a Movie":
    movie_name = st.sidebar.text_input("Enter a movie to find:")
    if st.sidebar.button("Find Movie"):
        results = find_movie(movie_name)
        st.write(results)

elif action == "Add a Movie":
    name = st.text_input("Enter the name of the movie:")
    genres = st.text_input("Enter genres separated by commas:").split(',')
    year = st.number_input("Enter the year:", min_value=1900, max_value=2023, step=1)
    run_time = st.number_input("Enter the run time in minutes:", min_value=1, max_value=500, step=1)
    rating = st.slider("Enter the rating (1-10):", min_value=1.0, max_value=10.0, step=0.1)
    actors = st.text_input("Enter actors separated by commas:").split(',')
    if st.button("Add Movie"):
        result = add_movie(name, genres, year, run_time, rating, actors)
        st.success(result)
