CREATE TABLE news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    text TEXT,
    subject TEXT,
    date TEXT,
    label TEXT -- 'Fake' or 'Real'
);

CREATE TABLE cleanedText (
    id INTEGER,
    cleaned_text TEXT,
    label TEXT,
    FOREIGN KEY(id) REFERENCES news(id)
);
