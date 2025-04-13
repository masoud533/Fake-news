import os
import re
import nltk
import json
import pickle
import tkinter
import numpy as np
from tkinter import *
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

modelPath = os.path.join('..', 'Models', 'lrModel.model')
model = open(modelPath, 'rb')
LR = pickle.load(model)
model.close()

modelPath = os.path.join('..', 'Models', 'tfidf_vectorizer.model')
model = open(modelPath, 'rb')
V = pickle.load(model)
model.close()

# 2. Initialize stopwords, stemmer, and lemmatizer
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def predict_class(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    X = [" ".join(words)]
    x_v = V.transform(X)
    p = LR.predict(x_v)
    print(p)
    return 1


def send():
    msg = EntryBox.get("1.0", "end-1c").strip()
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        res = predict_class(msg)
        ChatLog.insert(END, "Result: " + res + '\n')
        ChatLog.config(state=DISABLED)
        ChatLog.YView(END)

base = Tk()
base.title("Fake News Detector")
base.geometry("450x550")
base.resizable(width=True, height=True)

ChatLog = Text(base,bd=0, bg="white", height="8", width="50", font="Arial")

ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=("Verdana", 12, "bold"), text="Run", width="12",height=5,
                    bd=0, bg='#32de97', activebackground='#3c9d9b', fg='#ffffff', command= send)

EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()



