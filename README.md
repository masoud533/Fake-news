Fake News Detection with Machine Learning

This project is focused on detecting fake news using various machine learning models. It involves a complete pipeline from raw data handling to model evaluation and optimization.

Project Workflow

1. Data Source & Collection

Dataset downloaded from Kaggle.

Contains real and fake news in CSV format with fields: title, text, subject, and date.



2. Database Integration

Data was loaded into an SQLite database for structured querying and ease of access.

All processing steps use the database instead of directly reading from CSV files.



3. Data Cleaning & Preprocessing

Removed duplicates and null values.

Text preprocessing included:

Lowercasing

Removing punctuation and stopwords

Lemmatization

Tokenization




4. Exploratory Data Analysis

Statistical summaries of class distributions.

Word frequency analysis for fake vs. real news.

Visualization of most common words and class imbalance.



5. Modeling

Trained multiple classifiers: Logistic Regression, SVM, Random Forest, Naive Bayes.

Evaluated with accuracy on both training and test datasets.



6. Overfitting Check

Compared train and test accuracy.

Performed 10-fold Cross Validation.

Analyzed learning curves to ensure generalization.



7. Hyperparameter Tuning

Used GridSearchCV for Logistic Regression.

Tuned regularization strength (C), penalty (L1, L2), and solver type.

Identified the best combination for highest cross-validation accuracy.
