import streamlit as st
import joblib 

st.title("Student placement")

model = joblib.load("lr_model.joblib")

cgpa = st.number_input("cgpa ", min_value=0.0)
iq= st.number_input("iq ", min_value=0.0 )

sample = [[cgpa,iq]]

if st.button("Predict"):
    
    prediction = model.predict(sample)
    st.success(f"Predicted placement : **{prediction}**")