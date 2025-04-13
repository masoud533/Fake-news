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

# Preprocessing tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def predict_class(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    X = [" ".join(words)]
    x_v = V.transform(X)
    p = LR.predict(x_v)[0]
    
    return "Fake" if p == 0 else "Real"

def send():
    msg = EntryBox.get("1.0", "end-1c").strip()
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        res = predict_class(msg)
        ChatLog.insert(END, "You: " + msg + '\n', "user")
        ChatLog.insert(END, "Result: " + res + '\n\n', "result_fake" if res == "Fake" else "result_real")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        EntryBox.delete("1.0", END)

# GUI Setup
base = Tk()
base.title("Fake News Detector")
base.geometry("500x600")
base.resizable(width=False, height=False)
base.configure(bg="#f2f2f2")

# Chat log
ChatLogFrame = Frame(base, bg="#f2f2f2")
ChatLog = Text(ChatLogFrame, bd=0, bg="white", height="20", width="60", font=("Helvetica", 12), wrap=WORD)
ChatLog.tag_config("user", foreground="black", font=("Helvetica", 12, "bold"))
ChatLog.tag_config("result_real", foreground="green", font=("Helvetica", 12, "bold"))
ChatLog.tag_config("result_fake", foreground="red", font=("Helvetica", 12, "bold"))
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(ChatLogFrame, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

ChatLogFrame.pack(pady=10)
scrollbar.pack(side=RIGHT, fill=Y)
ChatLog.pack(side=LEFT, fill=BOTH, expand=True)

# Entry box and button
BottomFrame = Frame(base, bg="#f2f2f2")
EntryBox = Text(BottomFrame, bd=0, bg="white", width="40", height="4", font=("Helvetica", 12))
SendButton = Button(BottomFrame, text="Detect", font=("Helvetica", 12, "bold"), width="10", height=2,
                    bd=0, bg='#32de97', activebackground='#3c9d9b', fg='white', command=send)

BottomFrame.pack(pady=10)
EntryBox.grid(row=0, column=0, padx=10, pady=5)
SendButton.grid(row=0, column=1, padx=5)

base.mainloop()



