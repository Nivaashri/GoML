Airline Review Sentiment Analysis

Overview
     This project analyzes airline reviews to determine whether a customer recommends the airline or not. It uses Natural Language Processing (NLP) techniques and Logistic Regression for classification.

Installation
    1️.Prerequisites
        Ensure you have Python 3.7+ installed on your system. You will also need the following Python libraries:
          pandas
          numpy
          scikit-learn
          imbalanced-learn
    2.Install Dependencies
        Run the following command to install the required libraries:
            pip install pandas numpy scikit-learn imbalanced-learn
            python sentiment_analysis.py
    3.Dataset
        Ensure that you have a dataset file named AirlineReviews.csv in the same directory as your script. The dataset should contain the following columns:
    Review: The text of the airline review.
    Recommended: Labels indicating whether the airline is recommended ("yes" or "no").

Running the Code
    To train and evaluate the model, run the script:
        python sentiment_analysis.py
    Once the model is trained, you can enter airline reviews interactively, and the system will predict whether the sentiment is Positive ✅ or Negative ❌

Approach for Multi-Agent Function Calling 
    The project could be expanded to include multi-agent function calling, where different agents handle specific tasks:
    Data Preprocessing Agent – Handles text cleaning, negation handling, and vectorization.
    Model Training Agent – Trains the logistic regression model and evaluates performance.
    Prediction Agent – Takes new reviews and predicts sentiment based on trained models.
    This modular approach makes the system more scalable and adaptable for future improvements, such as integrating deep learning models.

Features
   ✅ Handles negations (e.g., "not good" → "bad")
   ✅ Uses TF-IDF vectorization with n-grams for text representation
   ✅ Applies SMOTE to handle class imbalance
   ✅ Uses Logistic Regression for classification
   ✅ Provides an interactive prompt for review predictions

Model Performance
  The model's performance is evaluated using:
     Accuracy Score
     Classification Report (Precision, Recall, F1-score)

