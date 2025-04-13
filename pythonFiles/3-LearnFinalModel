import os
import pickle
import sqlite3
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

# Connect to database
path = os.path.join('..', 'Database', 'news.db')
conn = sqlite3.connect(path)
cursor = conn.cursor()

# Load TF-IDF features
cursor.execute("SELECT data FROM features WHERE type = 'tfidf'")
X_tfidf_compressed = cursor.fetchone()[0]
X_tfidf = pickle.loads(X_tfidf_compressed)
print("Features loaded successfully!")

# Load labels from the original dataset
df= pd.read_sql("SELECT id, label FROM cleanedText", conn) 
df['label'] = df['label'].apply(lambda x: 1 if x == 'real' else (0 if x == 'fake' else None))

# Assuming X_tfidf is the extracted features
y = df['label'].values # Labels (0: Fake, 1: Real) 

# Split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=4893)
print("Data split into training and testing sets!")

# Train onest model (Logistic Regression)
lr_model = LogisticRegression(C=21.5443, penalty='l1', solver='liblinear')
lr_model.fit(X_train, y_train)


path = os.path.join('..', 'Models', 'lrModel.model')
with open(path, 'wb') as f:
    pickle.dump(lr_model, f)