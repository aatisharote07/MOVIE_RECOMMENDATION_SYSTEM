# 🎬 **Movie Recommendation System — CineMatch**

Welcome to **CineMatch**, your personal movie buddy! 🍿  
Built as part of our **academic mini-project**, this system recommends movies similar to your favorites using smart **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques. 🚀  

---

## 🌟 **Project Highlights**

✅ **Content-Based Filtering** — Recommends movies purely based on metadata such as *genres, keywords, cast, crew,* and *overview*.  
🧠 **NLP Techniques** — Includes *tokenization*, *stemming*, and *vectorization* using the **Bag-of-Words model**.  
📏 **Cosine Similarity** — Measures similarity between movies based on their feature vectors.  
💻 **Interactive Web App** — Built using **Flask** and **TailwindCSS** for a clean and responsive user interface.  
🎞️ **Dynamic Posters** — Fetches real-time movie posters from the **TMDB API**.  
🎯 **Top 10 Recommendations** — Displays the ten most similar movies for any selected title.

---

## 🛠️ **Tech Stack**

| Component | Technology |
|------------|-------------|
| **Language** | Python 3.7+ |
| **Framework** | Flask |
| **Frontend** | HTML, Tailwind CSS |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Serialization** | Pickle |
| **API** | TMDB API |

---

## 🚀 **Run Locally**

Follow these simple steps to get the app running on your system 👇

### 1️⃣ Clone the Repository
 
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Flask App
python app.py

4️⃣ Open in Browser

Go to 👉 http://127.0.0.1:5000

📂 Project Structure
movie-recommendation-system/
│

├── app.py                # Flask backend logic

├── index.html            # Frontend (TailwindCSS + Jinja2 template)

├── movie_list.pkl        # Pickled movie metadata

├── similarity.pkl        # Pickled similarity matrix

├── notebook.ipynb        # Data preprocessing & model building

├── static/               # Static files (images, CSS, JS)

├── requirements.txt      # Dependencies

└── README.md             # Project documentation

🎯 Key Features

✨ Search for any movie from the list
✨ Get Top 10 similar movies instantly with posters
✨ Light/Dark Mode support 🌗
✨ Beautiful 3D animated movie cards 🎥
✨ Genre popularity insights using charts 📊
✨ Fully responsive and modern UI

🔮 Future Enhancements

🚀 Add Collaborative Filtering for personalized recommendations
💬 Include user ratings and reviews
🧠 Implement Word2Vec / BERT-based embeddings for smarter suggestions
📈 Enable real-time recommendations based on user mood or current trends
🌍 Deploy the app on Heroku / AWS for public access

🧑‍💻 Authors

Aatish Ramdas Arote
Viraj Vilas Gawari
Department of Computer Engineering,
Konkan Gyanpeeth College of Engineering, Karjat

📜 License

This project is licensed under the MIT License.
