import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit app title
st.title("Student Performance Predictor")

# Sidebar or form inputs
st.header("Enter Student Information")

# Collect input using Streamlit widgets
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", min_value=0.0, max_value=100.0, value=70.0)
writing_score = st.number_input("Writing Score", min_value=0.0, max_value=100.0, value=70.0)

# Predict button
if st.button("Predict Performance"):
    try:
        # Create input data
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        df = data.get_data_as_data_frame()
        st.write("### Input Data", df)

        # Predict
        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)
        st.success(f"Predicted Math Score: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
