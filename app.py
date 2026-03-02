import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Student Exam Score Predictor", page_icon="🎓", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("🎓 Student Exam Score Predictor")
st.markdown("Enter student details below to predict the expected exam score.")

st.subheader("📋 Student Information")

col1, col2 = st.columns(2)

with col1:
    academic_level = st.selectbox("Academic Level", ["High School", "Undergraduate", "Postgraduate"])
    academic_level_encoded = {"High School": 0, "Undergraduate": 1, "Postgraduate": 2}[academic_level]

    study_hours = st.slider("Study Hours (per day)", 0.0, 12.0, 4.0, 0.1)
    self_study_hours = st.slider("Self Study Hours (per day)", 0.0, 10.0, 2.0, 0.1)
    online_classes_hours = st.slider("Online Classes Hours (per day)", 0.0, 10.0, 2.0, 0.1)
    sleep_hours = st.slider("Sleep Hours (per day)", 3.0, 12.0, 7.0, 0.1)

with col2:
    social_media_hours = st.slider("Social Media Hours (per day)", 0.0, 10.0, 2.0, 0.1)
    gaming_hours = st.slider("Gaming Hours (per day)", 0.0, 10.0, 1.0, 0.1)
    screen_time_hours = st.slider("Screen Time Hours (per day)", 0.0, 16.0, 5.0, 0.1)
    mental_health_score = st.slider("Mental Health Score (1–10)", 1, 10, 7)
    productivity_score = st.slider("Productivity Score (0–100)", 0.0, 100.0, 60.0, 0.5)

if st.button("🔮 Predict Exam Score", use_container_width=True):
    input_data = pd.DataFrame([{
        "academic_level": academic_level_encoded,
        "study_hours": study_hours,
        "self_study_hours": self_study_hours,
        "online_classes_hours": online_classes_hours,
        "social_media_hours": social_media_hours,
        "gaming_hours": gaming_hours,
        "sleep_hours": sleep_hours,
        "screen_time_hours": screen_time_hours,
        "mental_health_score": mental_health_score,
        "productivity_score": productivity_score
    }])

    prediction = model.predict(input_data)[0]
    prediction = np.clip(prediction, 0, 100)

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.metric("Predicted Exam Score", f"{prediction:.1f} / 100")

    if prediction >= 75:
        st.success("🌟 Excellent performance expected!")
    elif prediction >= 50:
        st.info("📘 Average performance expected. There's room to improve!")
    else:
        st.warning("⚠️ Below average score expected. Consider improving study habits.")

st.markdown("---")
st.caption("Model: Linear Regression | MAE ≈ 4.19 | Trained on 5000 student records")
