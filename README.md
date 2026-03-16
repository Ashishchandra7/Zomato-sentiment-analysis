📊 Zomato Review Sentiment Analysis
📌 Project Overview

This project focuses on analyzing customer reviews from Zomato to automatically determine whether a review expresses positive, neutral, or negative sentiment.

The objective is to build a machine learning model that can understand customer feedback and classify sentiment automatically, helping restaurants analyze customer satisfaction and improve service quality.

🎯 Problem Statement

Zomato receives thousands of reviews daily. Manually analyzing these reviews is difficult and time-consuming.

The goal of this project is to develop an NLP-based sentiment analysis model that can automatically classify reviews into Positive, Neutral, or Negative categories.

📂 Dataset

The dataset contains information about restaurant reviews and ratings.

Main Features:
Feature	Description
review	Customer review text
rating	Rating given by customer
sentiment	Sentiment label (Positive, Neutral, Negative)

🔎 Exploratory Data Analysis (EDA)

Several visualizations were created to understand patterns in the dataset.

Key insights:

• Majority of reviews are positive
• Negative reviews tend to contain more descriptive words
• Customer ratings strongly correlate with review sentiment

Example visualizations used:
Sentiment distribution
Word cloud analysis
Review length distribution
Correlation heatmap

⚙️ Data Preprocessing

Text data was cleaned and prepared using the following steps:

Converting text to lowercase
Removing punctuation
Removing stopwords
Lemmatization

These steps improve model performance by reducing noise in the text data.

🔢 Feature Engineering

Customer review text was converted into numerical features using:
TF-IDF helps capture the importance of words in the reviews.

🤖 Machine Learning Models

The following models were trained and evaluated:

Model	Purpose
Logistic Regression	Effective baseline for text classification
Random Forest Classifier	Captures complex relationships

Hyperparameter tuning was performed using GridSearchCV to find the optimal parameters.

📈 Model Evaluation

Evaluation metrics used:

Accuracy
Precision
Recall
F1 Score

Best Model Performance
Accuracy: ~95%
The Logistic Regression model performed best for sentiment classification.

🚀 Model Deployment

The trained model was saved using Joblib and deployed using Streamlit to create an interactive web application.

Users can enter a restaurant review and instantly receive the predicted sentiment.

Example:
Input: The food was amazing and service was great
Output: Positive

🛠 Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Natural Language Processing (NLP)
TF-IDF Vectorization
Logistic Regression
Random Forest
GridSearchCV
Joblib
Streamlit

🌐 Live Application

Streamlit App: https://zomato-sentiment-analysis-tzfgfnfjftwupawgwjtnsq.streamlit.app/
