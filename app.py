import streamlit as st
import pickle
import pandas as pd

# Load model and feature columns
model = pickle.load(open("model.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="AI Nutrition Deficiency Prediction",
    page_icon="🥗",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #34495e;
        text-align: center;
        margin-bottom: 25px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #d4edda;
        color: #155724;
        font-size: 24px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "About"])

# Home Page
if page == "Home":
    st.markdown('<div class="title">🥗 AI-Based Nutrition Deficiency Prediction System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Advanced symptom-based healthcare prediction using Machine Learning</div>', unsafe_allow_html=True)

    st.write("""
    ### Features:
    - Expanded symptom analysis
    - Realistic healthcare prediction
    - AI-powered deficiency detection
    - Improved predictive model
    - User-friendly dashboard
    """)

# Prediction Page
elif page == "Prediction":
    st.markdown('<div class="title">Nutrition Deficiency Prediction</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
        gender = st.selectbox("Gender", ["Male", "Female"])
        fatigue = st.selectbox("Fatigue?", ["No", "Yes"])
        hair_loss = st.selectbox("Hair loss?", ["No", "Yes"])
        bone_pain = st.selectbox("Bone pain?", ["No", "Yes"])
        weakness = st.selectbox("Weakness?", ["No", "Yes"])

    with col2:
        low_sunlight = st.selectbox("Low sunlight exposure?", ["No", "Yes"])
        vegetarian = st.selectbox("Vegetarian diet?", ["No", "Yes"])
        appetite_loss = st.selectbox("Appetite loss?", ["No", "Yes"])
        dizziness = st.selectbox("Dizziness?", ["No", "Yes"])
        muscle_cramps = st.selectbox("Muscle cramps?", ["No", "Yes"])
        skin_dryness = st.selectbox("Skin dryness?", ["No", "Yes"])
        memory_issues = st.selectbox("Memory issues?", ["No", "Yes"])

    # Convert values
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

    if st.button("Predict Deficiency"):
        prediction = model.predict(input_data)[0]

        st.markdown(
            f'<div class="prediction-box">Predicted Nutritional Deficiency: {prediction}</div>',
            unsafe_allow_html=True
        )

        # Risk score
        symptom_score = sum(input_data.iloc[0][[
            "Fatigue", "HairLoss", "BonePain", "Weakness",
            "LowSunlight", "Vegetarian", "AppetiteLoss",
            "Dizziness", "MuscleCramps", "SkinDryness", "MemoryIssues"
        ]])

        st.progress(min(symptom_score / 11, 1.0))
        st.metric("Risk Score", f"{symptom_score}/11")

        # Recommendations
        if prediction == "Iron":
            st.warning("Increase spinach, beans, lentils, red meat, and iron-rich foods.")
        elif prediction == "Vitamin D":
            st.warning("Increase sunlight exposure, fish, eggs, and fortified dairy.")
        elif prediction == "Calcium":
            st.warning("Consume milk, yogurt, almonds, and leafy greens.")
        elif prediction == "Protein":
            st.warning("Focus on eggs, legumes, chicken, nuts, and dairy.")
        elif prediction == "B12":
            st.warning("Consume dairy, eggs, fish, and fortified cereals.")

# About Page
elif page == "About":
    st.markdown('<div class="title">About This Project</div>', unsafe_allow_html=True)

    st.write("""
    ### Objective:
    Predict nutritional deficiencies using expanded symptom analysis and machine learning.

    ### Technologies:
    - Python
    - Streamlit
    - Scikit-learn
    - Pandas

    ### Deficiencies Covered:
    - Iron
    - Vitamin D
    - Calcium
    - Protein
    - Vitamin B12

    ### Benefits:
    - Preventive healthcare
    - Early awareness
    - User-friendly AI diagnosis
    """)