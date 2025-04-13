import os
import re
import nltk
import json
import pickle
import tkinter
import sqlite3
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

stopWords = nltk.corpus.stopwords.words('english')





base = Tk()
base.title("Hello")
base.geometry("450x550")
base.resizable(width=True, height=True)

ChatLog = Text(base,bd=0, bg="white", height="8", width="50", font="Arial")

ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#SendButton = Button(base, font=("Verdana", 12, "bold"), text="Send", width="12",height=5,
#                    bd=0, bg='#32de97', activebackground='#3c9d9b', fg='#ffffff', command= send)

#EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
#EntryBox.bind_all("<Key>", _onKeyRelease, "+")



