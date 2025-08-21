import os
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Debugging: print the current working directory
print("Current working directory:", os.getcwd())

# Load dataset with full path
df = pd.read_csv(
    r"C:\CODEXINTERN\Task's\AI-ML internship assignment\SMSSpamCollection",
    sep='\t',
    names=['label', 'message'],
    encoding='latin-1'   # helps with special characters
)

# Basic preprocessing: lowercase + remove punctuation
df['message'] = df['message'].str.lower().str.replace('[%s]' % string.punctuation, '', regex=True)

# Features (X) and labels (y)
X = df['message']
y = df['label'].map({'ham': 0, 'spam': 1})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vect, y_train)

# Predictions
y_pred = clf.predict(X_test_vect)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
