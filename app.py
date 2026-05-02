import streamlit as st
import pickle
import pandas as pd

# Load model and feature columns
model = pickle.load(open("model.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

# Page configuration
st.set_page_config(
    page_title="NutriAI Deficiency Predictor",
    page_icon="🥗",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
    background-color: #f4f9f9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

header, footer, [data-testid="stSidebar"] {
    display: none;
}

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #14532d;
    margin-bottom: 0;
}

.sub-title {
    text-align: center;
    font-size: 20px;
    color: #4b5563;
    margin-bottom: 30px;
}

.logo {
    text-align: center;
    font-size: 70px;
    margin-bottom: 10px;
}

.prediction-box {
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(135deg, #d1fae5, #bbf7d0);
    color: #14532d;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-top: 25px;
}

.recommendation-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #fef9c3;
    color: #854d0e;
    font-size: 18px;
    margin-top: 15px;
}

div.stButton > button {
    background-color: #16a34a;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px 30px;
    border: none;
}

div.stButton > button:hover {
    background-color: #15803d;
}

.metric-card {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="logo">🥗</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">NutriAI Deficiency Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart AI-powered nutritional health analysis</div>', unsafe_allow_html=True)

# Input Form
st.write("### Enter Your Health Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    fatigue = st.selectbox("Fatigue?", ["No", "Yes"])
    hair_loss = st.selectbox("Hair Loss?", ["No", "Yes"])
    bone_pain = st.selectbox("Bone Pain?", ["No", "Yes"])
    weakness = st.selectbox("Weakness?", ["No", "Yes"])

with col2:
    low_sunlight = st.selectbox("Low Sunlight Exposure?", ["No", "Yes"])
    vegetarian = st.selectbox("Vegetarian Diet?", ["No", "Yes"])
    appetite_loss = st.selectbox("Appetite Loss?", ["No", "Yes"])
    dizziness = st.selectbox("Dizziness?", ["No", "Yes"])
    muscle_cramps = st.selectbox("Muscle Cramps?", ["No", "Yes"])
    skin_dryness = st.selectbox("Skin Dryness?", ["No", "Yes"])
    memory_issues = st.selectbox("Memory Issues?", ["No", "Yes"])

# Convert inputs
def yes_no(val):
    return 1 if val == "Yes" else 0

input_data = pd.DataFrame([{
    "Age": age,
    "Fatigue": yes_no(fatigue),
    "HairLoss": yes_no(hair_loss),
    "BonePain": yes_no(bone_pain),
    "Weakness": yes_no(weakness),
    "LowSunlight": yes_no(low_sunlight),
    "Vegetarian": yes_no(vegetarian),
    "AppetiteLoss": yes_no(appetite_loss),
    "Dizziness": yes_no(dizziness),
    "MuscleCramps": yes_no(muscle_cramps),
    "SkinDryness": yes_no(skin_dryness),
    "MemoryIssues": yes_no(memory_issues),
    "Gender_Female": 1 if gender == "Female" else 0,
    "Gender_Male": 1 if gender == "Male" else 0
}])

# Align columns
input_data = input_data.reindex(columns=feature_columns, fill_value=0)

# Prediction
if st.button("Predict Deficiency"):
    prediction = model.predict(input_data)[0]

    st.markdown(
        f'<div class="prediction-box">Predicted Nutritional Deficiency: {prediction}</div>',
        unsafe_allow_html=True
    )

    # Risk Score
    symptom_score = sum(input_data.iloc[0][[
        "Fatigue", "HairLoss", "BonePain", "Weakness",
        "LowSunlight", "Vegetarian", "AppetiteLoss",
        "Dizziness", "MuscleCramps", "SkinDryness", "MemoryIssues"
    ]])

    st.progress(min(symptom_score / 11, 1.0))
    st.metric("Health Risk Score", f"{symptom_score}/11")

    # Recommendations
    recommendations = {
        "Iron": "Increase spinach, beans, lentils, red meat, and iron-rich foods.",
        "Vitamin D": "Increase sunlight exposure, fish, eggs, and fortified dairy.",
        "Calcium": "Consume milk, yogurt, almonds, and leafy greens.",
        "Protein": "Focus on eggs, legumes, chicken, nuts, and dairy.",
        "B12": "Consume dairy, eggs, fish, and fortified cereals."
    }

    st.markdown(
        f'<div class="recommendation-box">{recommendations[prediction]}</div>',
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.caption("Developed with AI & Machine Learning for preventive nutritional healthcare")

