import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="AI Nutrition Deficiency Prediction",
    page_icon="🥗",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #34495e;
        text-align: center;
        margin-bottom: 30px;
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
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "About"])

# Home Page
if page == "Home":
    st.markdown('<div class="title">🥗 AI-Based Nutrition Deficiency Prediction System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Smart healthcare powered by Machine Learning</div>', unsafe_allow_html=True)

    st.write("""
    ### Key Features:
    - Symptom-based AI prediction
    - Personalized nutritional analysis
    - Health awareness support
    - User-friendly healthcare dashboard
    """)

    st.info("This software helps identify potential nutritional deficiencies early for preventive healthcare.")

# Prediction Page
elif page == "Prediction":
    st.markdown('<div class="title">Nutrition Deficiency Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Fill in your health details below</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
        gender = st.selectbox("Gender", ["Male", "Female"])
        fatigue = st.selectbox("Do you experience fatigue?", ["No", "Yes"])
        hair_loss = st.selectbox("Hair loss?", ["No", "Yes"])
        bone_pain = st.selectbox("Bone pain?", ["No", "Yes"])

    with col2:
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

    if st.button("Predict Deficiency"):
        prediction = model.predict(input_data)[0]

        st.markdown(f'<div class="prediction-box">Predicted Nutritional Deficiency: {prediction}</div>', unsafe_allow_html=True)

        # Severity score
        symptom_score = sum([
            fatigue_val, hair_loss_val, bone_pain_val,
            weakness_val, sunlight_val, vegetarian_val, appetite_val
        ])

        st.progress(min(symptom_score / 7, 1.0))

        st.metric("Risk Score", f"{symptom_score}/7")

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
    ### Project Objective:
    This AI-powered system predicts nutritional deficiencies using symptom analysis and machine learning.

    ### Technologies Used:
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

    ### Purpose:
    Early health awareness and preventive nutrition support.
    """)

    st.success("Developed as an AI mini project for healthcare innovation.")
