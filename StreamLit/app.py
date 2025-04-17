import streamlit as st
import os
import re
import nltk
import pickle
import tkinter as tk
from tkinter import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Load models
with open(os.path.join('..', 'Models', 'lrModel.model'), 'rb') as model_file:
    LR = pickle.load(model_file)

with open(os.path.join('..', 'Models', 'tfidf_vectorizer.model'), 'rb') as vectorizer_file:
    V = pickle.load(vectorizer_file)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

st.title('Fake or Real News Detection with AI!')

text = st.text_area("Enter your news text: ")

btn = st.button("Detect")

if btn:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    X = [" ".join(words)]
    x_v = V.transform(X)
    p = LR.predict(x_v)[0]
    result =  "Fake" if p == 0 else "Real"
    st.success("This News is: " + result)