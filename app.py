import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# App title
st.title("AI-Based Nutrition Deficiency Prediction System")

st.write("Enter your symptoms and lifestyle details below:")

# User inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)

gender = st.selectbox("Gender", ["Male", "Female"])
fatigue = st.selectbox("Fatigue", [0, 1])
hair_loss = st.selectbox("Hair Loss", [0, 1])
bone_pain = st.selectbox("Bone Pain", [0, 1])
weakness = st.selectbox("Weakness", [0, 1])
low_sunlight = st.selectbox("Low Sunlight Exposure", [0, 1])
vegetarian = st.selectbox("Vegetarian", [0, 1])
appetite_loss = st.selectbox("Appetite Loss", [0, 1])

# Prepare input
input_data = pd.DataFrame([{
    "Age": age,
    "Fatigue": fatigue,
    "HairLoss": hair_loss,
    "BonePain": bone_pain,
    "Weakness": weakness,
    "LowSunlight": low_sunlight,
    "Vegetarian": vegetarian,
    "AppetiteLoss": appetite_loss,
    "Gender_Female": 1 if gender == "Female" else 0,
    "Gender_Male": 1 if gender == "Male" else 0
}])

# Prediction
if st.button("Predict Deficiency"):
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Nutritional Deficiency: {prediction[0]}")

    # Basic suggestions
    if prediction[0] == "Iron":
        st.info("Suggested focus: Iron-rich foods like spinach, lentils, red meat.")
    elif prediction[0] == "Vitamin D":
        st.info("Suggested focus: Sunlight exposure, eggs, fish, fortified dairy.")
    elif prediction[0] == "Calcium":
        st.info("Suggested focus: Milk, yogurt, cheese, leafy greens.")
    elif prediction[0] == "Protein":
        st.info("Suggested focus: Eggs, legumes, chicken, nuts.")
    elif prediction[0] == "B12":
        st.info("Suggested focus: Dairy, eggs, fish, fortified cereals.")