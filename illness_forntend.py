# 1. IMPORT LIBRARIES

import streamlit as st
import pandas as pd
import joblib
import os


# 2. PAGE CONFIGURATION

st.set_page_config(
    page_title="Common Illness Disease Prediction System",
    page_icon="🏥",
    layout="centered"
)


# 3. LOAD MODEL AND SCALER

@st.cache_resource
def load_model():

    if not os.path.exists("health_model.pkl"):
        st.error("❌ health_model.pkl not found.")
        st.stop()

    if not os.path.exists("health_scaler.pkl"):
        st.error("❌ health_scaler.pkl not found.")
        st.stop()

    model = joblib.load("health_model.pkl")
    scaler = joblib.load("health_scaler.pkl")

    return model, scaler


model, scaler = load_model()


# ============================================================
# 4. HEADER
# ============================================================

st.title("🏥 Common Illness Disease Prediction System")

st.write(
    "AI-powered preliminary prediction of common illnesses "
    "using common health symptoms."
)

st.divider()


# ============================================================
# 5. ABOUT
# ============================================================

st.subheader("📌 About")

st.write(
    "This system analyzes five health-related features — "
    "Fever, Headache, Cough, Fatigue, and Body Pain — "
    "and predicts a possible illness using a trained "
    "Logistic Regression machine learning model."
)


# ============================================================
# 6. PATIENT INFORMATION
# ============================================================

st.subheader("👤 Patient Information")


# ------------------------------------------------------------
# Fever
# ------------------------------------------------------------

fever = st.number_input(
    "🌡️ Fever (°F)",
    min_value=90.0,
    max_value=110.0,
    value=103.6,
    step=0.1
)


# ------------------------------------------------------------
# Headache
# ------------------------------------------------------------

headache = st.number_input(
    "🤕 Headache Severity (0–10)",
    min_value=0.0,
    max_value=10.0,
    value=8.7,
    step=0.1
)


# ------------------------------------------------------------
# Cough
# ------------------------------------------------------------

cough = st.number_input(
    "😷 Cough Severity (0–10)",
    min_value=0.0,
    max_value=10.0,
    value=2.9,
    step=0.1
)


# ------------------------------------------------------------
# Fatigue
# ------------------------------------------------------------

fatigue = st.number_input(
    "😴 Fatigue Severity (0–10)",
    min_value=0.0,
    max_value=10.0,
    value=6.5,
    step=0.1
)


# ------------------------------------------------------------
# Body Pain
# ------------------------------------------------------------

body_pain = st.number_input(
    "💪 Body Pain Severity (0–10)",
    min_value=0.0,
    max_value=10.0,
    value=2.2,
    step=0.1
)


# ============================================================
# 7. PREDICT BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Disease",
    use_container_width=True
)


# ============================================================
# 8. PREDICTION
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # Create input DataFrame
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        {
            "Fever": [fever],
            "Headache": [headache],
            "Cough": [cough],
            "Fatigue": [fatigue],
            "Body_Pain": [body_pain]
        }
    )


    # --------------------------------------------------------
    # Match training feature order
    # --------------------------------------------------------

    if hasattr(scaler, "feature_names_in_"):

        input_data = input_data[
            list(scaler.feature_names_in_)
        ]


    # --------------------------------------------------------
    # Scale input
    # --------------------------------------------------------

    try:

        input_scaled = scaler.transform(
            input_data
        )

    except Exception as e:

        st.error(
            "❌ Error while processing input."
        )

        st.write(e)

        st.stop()


    # --------------------------------------------------------
    # Make prediction
    # --------------------------------------------------------

    try:

        prediction = model.predict(
            input_scaled
        )[0]

    except Exception as e:

        st.error(
            "❌ Error while making prediction."
        )

        st.write(e)

        st.stop()


    # --------------------------------------------------------
    # Calculate probabilities
    # --------------------------------------------------------

    probability = None
    confidence = None

    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(
            input_scaled
        )[0]

        confidence = max(probability) * 100


    # ========================================================
    # 9. DISPLAY RESULT
    # ========================================================

    st.divider()

    st.subheader("🎯 Prediction Result")

    st.success(
        f"Predicted Disease: {prediction}"
    )


    # ========================================================
    # 13. HEALTH GUIDANCE
    # ========================================================

    st.subheader("🩺 General Health Guidance")

    st.write(
        "💧 Stay hydrated and get adequate rest."
    )

    st.write(
        "🔍 Monitor your symptoms regularly."
    )

    st.write(
        "👨‍⚕️ Consult a qualified healthcare professional "
        "for proper evaluation."
    )

    st.write(
        "💊 Do not start or stop medication without "
        "professional medical advice."
    )


# ============================================================
# 14. FOOTER
# ============================================================

st.divider()

st.caption(
    "⚕️ This application is for educational and preliminary "
    "prediction purposes only."
)