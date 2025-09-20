#Create a simple recommendation system that suggests items to users based on their preferences. You can use techniques like collaborative filtering or content-based filtering to recommend movies, books, or products to users

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    'title': [
        'The Matrix', 'The Lord of the Rings', 'Harry Potter',
        'Inception', 'Interstellar', 'The Dark Knight'
    ],
    'genre': [
        'Action Sci-Fi', 'Adventure Fantasy', 'Fantasy Magic',
        'Action Sci-Fi', 'Adventure Sci-Fi', 'Action Thriller'
    ]
}

df = pd.DataFrame(data)

# Convert genres to TF-IDF features
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['genre'])

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(title, cosine_sim=cosine_sim):
    if title not in df['title'].values:
        return ["Item not found in database."]
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]
    recommended = [df.iloc[i[0]]['title'] for i in sim_scores]
    return recommended

# Example
print("Recommendations for Inception:", recommend("Inception"))
