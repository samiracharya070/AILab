import streamlit as st

import joblib

st.title("Iris Flower Classifier")

# Load model
model = joblib.load("knn_model.joblib")

# Inputs
sl = st.number_input("Sepal length", min_value=0.0, format="%.2f")
sw = st.number_input("Sepal width", min_value=0.0, format="%.2f")
pl = st.number_input("Petal length", min_value=0.0, format="%.2f")
pw = st.number_input("Petal width", min_value=0.0, format="%.2f")

# Prepare input (2D array)
sample = [[sl, sw, pl, pw]]

# Prediction
if st.button("Predict"):
    prediction = model.predict(sample)[0]  # returns 'Iris-versicolor'
    st.success(f"Predicted Iris species: **{prediction}**")