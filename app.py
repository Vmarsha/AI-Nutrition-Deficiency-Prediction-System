import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page configuration
st.set_page_config(
    page_title="AI-Based Nutrition Deficiency Prediction System",
    layout="centered"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "About"])

# Home Page
if page == "Home":
    st.title("AI-Based Nutrition Deficiency Prediction System")
    st.subheader("Predict potential nutritional deficiencies using AI")
    
    st.write("""
    ### Features:
    - Symptom-based prediction
    - AI-powered deficiency detection
    - Personalized health insights
    - Easy-to-use interface
    """)

# Prediction Page
elif page == "Prediction":
    st.title("Nutrition Deficiency Prediction")

    st.write("Fill in your health details below:")

    age = st.number_input("Age", min_value=1, max_value=100, value=25)

    gender = st.selectbox("Gender", ["Male", "Female"])
    fatigue = st.selectbox("Do you experience fatigue?", ["No", "Yes"])
    hair_loss = st.selectbox("Hair loss?", ["No", "Yes"])
    bone_pain = st.selectbox("Bone pain?", ["No", "Yes"])
    weakness = st.selectbox("Weakness?", ["No", "Yes"])
    low_sunlight = st.selectbox("Low sunlight exposure?", ["No", "Yes"])
    vegetarian = st.selectbox("Vegetarian diet?", ["No", "Yes"])
    appetite_loss = st.selectbox("Appetite loss?", ["No", "Yes"])

    # Convert inputs
    fatigue_val = 1 if fatigue == "Yes" else 0
    hair_loss_val = 1 if hair_loss == "Yes" else 0
    bone_pain_val = 1 if bone_pain == "Yes" else 0
    weakness_val = 1 if weakness == "Yes" else 0
    sunlight_val = 1 if low_sunlight == "Yes" else 0
    vegetarian_val = 1 if vegetarian == "Yes" else 0
    appetite_val = 1 if appetite_loss == "Yes" else 0

    # Input dataframe
    input_data = pd.DataFrame([{
        "Age": age,
        "Fatigue": fatigue_val,
        "HairLoss": hair_loss_val,
        "BonePain": bone_pain_val,
        "Weakness": weakness_val,
        "LowSunlight": sunlight_val,
        "Vegetarian": vegetarian_val,
        "AppetiteLoss": appetite_val,
        "Gender_Female": 1 if gender == "Female" else 0,
        "Gender_Male": 1 if gender == "Male" else 0
    }])

    # Prediction
    if st.button("Predict Deficiency"):
        prediction = model.predict(input_data)[0]

        st.success(f"Predicted Nutritional Deficiency: {prediction}")

        # Suggestions
        if prediction == "Iron":
            st.info("Possible signs indicate Iron deficiency. Focus on spinach, lentils, beans, red meat, and iron supplements.")
        elif prediction == "Vitamin D":
            st.info("Possible Vitamin D deficiency. Increase sunlight exposure, eggs, fish, and fortified dairy.")
        elif prediction == "Calcium":
            st.info("Possible Calcium deficiency. Consume milk, yogurt, cheese, almonds, and leafy greens.")
        elif prediction == "Protein":
            st.info("Possible Protein deficiency. Increase eggs, legumes, chicken, fish, and nuts.")
        elif prediction == "B12":
            st.info("Possible Vitamin B12 deficiency. Focus on dairy, eggs, fish, and fortified cereals.")

# About Page
elif page == "About":
    st.title("About This Project")

    st.write("""
    This AI-based software predicts possible nutritional deficiencies using machine learning.

    ### Technologies Used:
    - Python
    - Pandas
    - Scikit-learn
    - Streamlit

    ### Deficiencies Covered:
    - Iron
    - Vitamin D
    - Calcium
    - Protein
    - Vitamin B12

    ### Objective:
    Early detection of nutritional deficiencies for preventive healthcare.
    """)