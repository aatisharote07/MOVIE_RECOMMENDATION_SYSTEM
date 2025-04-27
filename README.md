# MOVIE_RECOMMENDATION_SYSTEM
🎬 Movie Recommendation System
Welcome to the Movie Recommendation System!
Built as a part of our academic mini-project, this system suggests movies similar to your favorites, using smart Natural Language Processing (NLP) and Machine Learning techniques. 🚀

📌 Project Highlights
Content-Based Filtering: Suggests movies purely based on metadata like genres, keywords, cast, crew, and overview.

NLP Techniques: Tokenization, stemming, and vectorization using the Bag-of-Words model.

Cosine Similarity: Measures how close two movies are, based on their feature vectors.

Interactive Web App: Simple and elegant frontend using Flask and TailwindCSS.

Dynamic Movie Posters: Fetches real-time posters from TMDB API.

Top 10 Recommendations: Displays the top 10 similar movies for any selected title.

🛠️ Tech Stack
Python 3.7+

Flask (for backend)

HTML + Tailwind CSS (for frontend)

Pickle (for serialized models)

Pandas, Scikit-learn, Numpy (for data processing and ML)

TMDB API (for fetching movie posters)

🚀 How to Run Locally
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask App

bash
Copy
Edit
python app.py
Open Your Browser
Go to: http://127.0.0.1:5000

📂 Project Structure
perl
Copy
Edit
movie-recommendation-system/
│
├── app.py                 # Flask backend logic
├── index.html              # Frontend (TailwindCSS + Jinja2 template)
├── movie_list.pkl          # Pickled movie metadata
├── similarity.pkl          # Pickled similarity matrix
├── notebook.ipynb          # Data preprocessing and model building
├── static/                 # Default images (optional)
├── README.md               # Project Documentation (this file!)
└── requirements.txt        # Project dependencies
🎯 Key Features
Search for any movie from the list.

Get instant top 10 similar movies with posters.

Light/Dark Mode Support.

3D animated movie cards.

Genre popularity insights using charts.

Responsive and modern UI.

🧠 Future Improvements
Add Collaborative Filtering for even better personalization.

Integrate user ratings and reviews.

Use deep learning (Word2Vec / BERT) for smarter recommendations.

Real-time updating based on user mood or recent trends.

Deploy online using Heroku or AWS.

📜 License
This project is licensed under the MIT License.

✨ Authors
Aatish Ramdas Arote 

Viraj Vilas Gawari 


Department of Computer Engineering,
Konkan Gyanpeeth College of Engineering, Karjat.

🌟 CineMatch — Your Personal Movie Buddy!

