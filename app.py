# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import joblib


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Kidney Disease Prediction",
    page_icon="🩺",
    layout="centered"
)


# ============================================================
# 3. LOAD TRAINED MODEL FILES
# ============================================================

model = joblib.load("kidney_model.pkl")
scaler = joblib.load("kidney_scaler.pkl")
columns = joblib.load("kidney_columns.pkl")


# ============================================================
# 4. APPLICATION HEADER
# ============================================================

st.title("🩺 Kidney Disease Prediction System")

st.write(
    "Enter patient health details to predict the possibility "
    "of Chronic Kidney Disease."
)

st.divider()


# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🩺 Kidney Disease Prediction")

    st.write(
        "AI-powered preliminary kidney disease prediction system."
    )

    st.divider()

    st.subheader("About")

    st.write(
        "This application predicts the possibility of Chronic "
        "Kidney Disease using selected health parameters."
    )


# ============================================================
# 6. KIDNEY DISEASE INPUT FORM
# ============================================================

st.subheader("Patient Information")


# Age
age = st.number_input(
    "Age",
    min_value=0,
    max_value=120,
    value=0,
    step=1
)


# Creatinine
creatinine = st.number_input(
    "Creatinine Level",
    min_value=0.0,
    max_value=20.0,
    value=0.0,
    step=0.1
)


# BUN
bun = st.number_input(
    "BUN Level",
    min_value=0.0,
    max_value=200.0,
    value=0.0,
    step=0.1
)


# Diabetes
diabetes = st.selectbox(
    "Do you have Diabetes?",
    ["No", "Yes"]
)

diabetes_value = 1 if diabetes == "Yes" else 0


# Hypertension
hypertension = st.selectbox(
    "Do you have Hypertension?",
    ["No", "Yes"]
)

hypertension_value = 1 if hypertension == "Yes" else 0


# GFR
gfr = st.number_input(
    "GFR",
    min_value=0.0,
    max_value=200.0,
    value=0.0,
    step=0.1
)


# Urine Output
urine_output = st.number_input(
    "Urine Output",
    min_value=0.0,
    max_value=5000.0,
    value=0.0,
    step=1.0
)


# ============================================================
# 7. PREDICT BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Kidney Disease",
    use_container_width=True
)


# ============================================================
# 8. PREDICTION
# ============================================================

if predict_button:

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Age": [age],
        "Creatinine_Level": [creatinine],
        "BUN": [bun],
        "Diabetes": [diabetes_value],
        "Hypertension": [hypertension_value],
        "GFR": [gfr],
        "Urine_Output": [urine_output]
    })


    # Arrange columns in training order
    input_data = input_data[columns]


    # Scale input
    input_scaled = scaler.transform(input_data)


    # Make prediction
    prediction = model.predict(input_scaled)[0]


    # ========================================================
    # 9. DISPLAY RESULT
    # ========================================================

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ CKD Detected")

    else:

        st.success("✅ Normal - No CKD Detected")


    # ========================================================
    # 10. HEALTH GUIDANCE
    # ========================================================

    st.subheader("💡 Health Guidance")

    if prediction == 1:

        st.write(
            "• 🩺 Consult a healthcare professional for proper kidney evaluation."
        )

        st.write(
            "• 💧 Follow appropriate hydration advice from your healthcare provider."
        )

        st.write(
            "• 🍬 Keep blood sugar under control if you have diabetes."
        )

        st.write(
            "• ❤️ Monitor and manage your blood pressure regularly."
        )

    else:

        st.write(
            "• 🥗 Maintain a healthy and balanced diet."
        )

        st.write(
            "• 💧 Stay adequately hydrated according to your health needs."
        )

        st.write(
            "• 🏃 Stay physically active and maintain a healthy lifestyle."
        )

        st.write(
            "• 🩺 Continue regular health checkups."
        )

