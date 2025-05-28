import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

df = pd.read_csv("AirlineReviews.csv")  
print("Column names:", df.columns)
if 'Recommended' not in df.columns or 'Review' not in df.columns:
    raise ValueError("Dataset must have 'Recommended' and 'Review' columns")
print("Class distribution:\n", df['Recommended'].value_counts())
df.dropna(subset=['Review'], inplace=True)  
df['Recommended'] = df['Recommended'].map({'yes': 1, 'no': 0})  
def handle_negations(text):
    negations = {
        "not good": "bad",
        "not bad": "good",
        "not happy": "unhappy",
        "not great": "terrible",
        "not terrible": "great",
        "not satisfied": "dissatisfied",
        "not recommend": "avoid"
    }
    for phrase, replacement in negations.items():
        text = re.sub(r'\b' + phrase + r'\b', replacement, text, flags=re.IGNORECASE)
    return text
df['Review'] = df['Review'].apply(handle_negations)

X = df['Review']  
y = df['Recommended'] 
vectorizer = TfidfVectorizer(stop_words='english', max_features=7000, ngram_range=(1, 3))  
X_vectorized = vectorizer.fit_transform(X)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_vectorized, y)
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
def predict_sentiment(text):
    text = handle_negations(text) 
    text_vectorized = vectorizer.transform([text])  
    prediction = model.predict(text_vectorized)[0]  
    return "Positive ✅" if prediction == 1 else "Negative ❌"
while True:
    user_input = input("\nEnter a review (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting... 👋")
        break
    prediction = predict_sentiment(user_input)
    print(f"Prediction: {prediction}")
