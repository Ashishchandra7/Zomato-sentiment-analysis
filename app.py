import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf.pkl")

st.title("Zomato Sentiment Analysis")

review = st.text_area("Enter Review")

if st.button("Predict Sentiment"):

    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)

    st.write("Sentiment:", prediction[0])