from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

# Load models
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "/static/default.jpg"

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    rec_names, rec_posters = [], []
    # Change the slice from [1:6] to [1:11] to get the top 10 recommendations (excluding the movie itself)
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        rec_names.append(movies.iloc[i[0]].title)
        rec_posters.append(fetch_poster(movie_id))
    return rec_names, rec_posters

# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    movie_list = movies['title'].values
    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        rec_names, rec_posters = recommend(selected_movie)
        return render_template('index.html', movie_list=movie_list, rec_names=rec_names, rec_posters=rec_posters, zip=zip)
    return render_template('index.html', movie_list=movie_list, rec_names=[], rec_posters=[], zip=zip)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
