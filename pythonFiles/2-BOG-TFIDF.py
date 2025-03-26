import os
import json
import pickle
import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer



# Connect to the database and load cleaned data
path = os.path.join('..', 'Database', 'news.db')
conn = sqlite3.connect(path)
df = pd.read_sql("SELECT * FROM cleanedText", conn)


# Initialize CountVectorizer (Bag of Words)
vectorizer = CountVectorizer(max_features=5000)  # Use top 5000 words
X_bow = vectorizer.fit_transform(df["cleaned_text"])

# Convert to DataFrame for better visualization
X_bow_df = pd.DataFrame(X_bow.toarray(), columns=vectorizer.get_feature_names_out())

print("Bag of Words Representation!!")

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf_vectorizer.fit_transform(df["cleaned_text"])

# Convert to DataFrame
X_tfidf_df = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

print("TF-IDF Representation!")

# Convert BoW and TF-IDF matrices to a compressed format
X_bow_compressed = pickle.dumps(X_bow)  # Convert to binary format
X_tfidf_compressed = pickle.dumps(X_tfidf)


cursor = conn.cursor()
# Create table for compressed features
cursor.execute("""
CREATE TABLE IF NOT EXISTS features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,  -- 'bow' or 'tfidf'
    data BLOB   -- Binary large object to store compressed data
)
""")

# Insert compressed features
cursor.execute("INSERT INTO features (type, data) VALUES (?, ?)", ("bow", X_bow_compressed))
cursor.execute("INSERT INTO features (type, data) VALUES (?, ?)", ("tfidf", X_tfidf_compressed))

# Commit
conn.commit()
print("Features compressed and saved to the database!")