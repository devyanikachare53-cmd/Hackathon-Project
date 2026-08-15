# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import joblib
import os


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Common Illness Disease Prediction System ",
    page_icon="🏥",
    layout="centered"
)


# ============================================================
# 3. LOAD TRAINED MODEL AND SCALER
# ============================================================

@st.cache_resource
def load_model():

    # Load trained model
    if os.path.exists("health model_pkl"):
        model = joblib.load("health model_pkl")

    elif os.path.exists("health_model.pkl"):
        model = joblib.load("health_model.pkl")

    else:
        st.error(
            "❌ Model file not found. "
            "Please check the model filename."
        )
        st.stop()

    # Load scaler
    if os.path.exists("health_scaler.pkl"):
        scaler = joblib.load("health_scaler.pkl")

    else:
        st.error(
            "❌ health_scaler.pkl not found."
        )
        st.stop()

    return model, scaler


model, scaler = load_model()


# ============================================================
# 4. APPLICATION HEADER
# ============================================================

st.title("🏥Common Illness Disease Prediction System ")

st.write(
    "AI-powered preliminary prediction of common illnesses"
)

st.divider()


# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:

    st.header("Common Illness Disease Prediction System")

    st.write(
        "AI-powered preliminary disease prediction "
        "using common medical symptoms."
    )

    
    st.divider()

    st.subheader(" About")

    st.write(
    "This AI-powered system analyzes common health symptoms "
    "such as fever, headache, cough, fatigue, and body pain "
    "to predict a possible disease using a trained machine "
    "learning model."
    )
   

# ============================================================
# 6. PATIENT INFORMATION
# ============================================================

st.subheader("Patient Information")


# ------------------------------------------------------------
# Fever
# ------------------------------------------------------------

fever = st.number_input(
    "Fever (%)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0
)


# ------------------------------------------------------------
# Headache
# ------------------------------------------------------------

headache = st.selectbox(
    "Headache",
    [
        "No",
        "Yes"
    ]
)


# ------------------------------------------------------------
# Cough
# ------------------------------------------------------------

cough = st.selectbox(
    "Cough",
    [
        "No",
        "Yes"
    ]
)


# ------------------------------------------------------------
# Fatigue
# ------------------------------------------------------------

fatigue = st.selectbox(
    "Fatigue",
    [
        "No",
        "Yes"
    ]
)


# ------------------------------------------------------------
# Body Pain
# ------------------------------------------------------------

body_pain = st.selectbox(
    "Body Pain",
    [
        "No",
        "Yes"
    ]
)

fever_value = fever


if headache == "Yes":
    headache_value = 1
else:
    headache_value = 0


if cough == "Yes":
    cough_value = 1
else:
    cough_value = 0


if fatigue == "Yes":
    fatigue_value = 1
else:
    fatigue_value = 0


if body_pain == "Yes":
    body_pain_value = 1
else:
    body_pain_value = 0


# ============================================================
# 8. PREDICT BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "Predict Disease",
    use_container_width=True
)


# ============================================================
# 9. PREDICTION
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # Create input DataFrame
    #
    # IMPORTANT:
    # Body_Pain is used because this is what your scaler expects.
    # --------------------------------------------------------

    # input_data = pd.DataFrame(
    #     {
    #         "Fever": [fever_value],
    #         "Headache": [headache_value],
    #         "Cough": [cough_value],
    #         "Fatigue": [fatigue_value],
    #         "Body_Pain": [body_pain_value]
    #     }
    # )

    if predict_button:

    # ========================================================
    # CHECK IF NO SYMPTOMS ARE ENTERED
    # ========================================================

        if (
            fever == 0
            and headache == "No"
            and cough == "No"
            and fatigue == "No"
            and body_pain == "No"
        ):

            st.warning(
                "⚠️ Please enter at least one symptom to get a prediction."
            )

        else:

            # ----------------------------------------------------
            # Create input DataFrame
            # ----------------------------------------------------

            input_data = pd.DataFrame(
                {
                    "Fever": [fever_value],
                    "Headache": [headache_value],
                    "Cough": [cough_value],
                    "Fatigue": [fatigue_value],
                    "Body_Pain": [body_pain_value]
                }
            )


    # ========================================================
    # 10. MATCH TRAINING COLUMN ORDER
    # ========================================================

    try:

        if hasattr(scaler, "feature_names_in_"):

            scaler_columns = list(
                scaler.feature_names_in_
            )

            input_data = input_data[
                scaler_columns
            ]

    except Exception:

        pass


    # ========================================================
    # 11. SCALE INPUT DATA
    # ========================================================

    try:

        input_scaled = scaler.transform(
            input_data
        )

    except Exception as e:

        st.error(
            "Error while processing the input data."
        )

        st.write(
            "Model expects these features:"
        )

        if hasattr(scaler, "feature_names_in_"):

            st.write(
                list(scaler.feature_names_in_)
            )

        st.stop()


    # ========================================================
    # 12. MAKE PREDICTION
    # ========================================================

    try:

        prediction = model.predict(
            input_scaled
        )[0]

    except Exception as e:

        st.error(
            "Error while making prediction."
        )

        st.stop()


    # ========================================================
    # 13. PREDICTION PROBABILITY
    # ========================================================

    confidence = None

    if hasattr(model, "predict_proba"):

        try:

            probability = model.predict_proba(
                input_scaled
            )[0]

            confidence = (
                max(probability) * 100
            )

        except Exception:

            confidence = None


    # ========================================================
    # 14. DISPLAY RESULT
    # ========================================================

    st.divider()

    st.subheader("Prediction Result")


    # --------------------------------------------------------
    # Predicted Disease
    # --------------------------------------------------------

    st.success(
        f"Predicted Disease: {prediction}"
    )


    
    # ============================================================
    # HEALTH GUIDANCE
    # ============================================================

    st.subheader("🩺 Health Guidance")


    if prediction != "Normal Fever":

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

    else:

        st.write(
            "😊 No significant illness pattern was predicted."
        )

        st.write(
            "💧 Continue maintaining good hydration and rest."
        )

        st.write(
            "🥗 Maintain a balanced and healthy diet."
        )

        st.write(
            "🏃 Maintain regular healthy physical activity."
        )

        st.write(
            "🔍 Continue monitoring your health and symptoms."
        )