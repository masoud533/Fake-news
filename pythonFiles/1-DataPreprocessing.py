import os
import re
import nltk
import sqlite3
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# 1. Connect to the database and fetch data
path = os.path.join('..', 'Database', 'news.db')
conn = sqlite3.connect(path)
df = pd.read_sql("SELECT id, text, label FROM news", conn)

# 2. Initialize stopwords, stemmer, and lemmatizer
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer() 

def preprocess_text(text):
    # 3. Convert text to lowercase
    text = text.lower()
    
    # 4. Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    
    # 5. Tokenize text into words
    words = word_tokenize(text)
    
    # 6. Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # 7. Apply lemmatization (or stemming as an alternative)
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # 8. Convert the list of words back to a string
    return " ".join(words)

# Apply preprocessing to all text data
df["cleaned_text"] = df["text"].apply(preprocess_text)

df.drop(['text'], axis=1, inplace=True)
df = df.loc[:, ['id', 'cleaned_text', 'label']]

df.to_sql('cleanedText', conn, if_exists="append", index=False)