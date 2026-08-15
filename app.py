# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import joblib
<<<<<<< HEAD
import os
=======
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
<<<<<<< HEAD
    page_title="Common Illness Disease Prediction System ",
    page_icon="🏥",
=======
    page_title="Kidney Disease Prediction",
    page_icon="🩺",
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
    layout="centered"
)


# ============================================================
<<<<<<< HEAD
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
=======
# 3. LOAD TRAINED MODEL FILES
# ============================================================

model = joblib.load("kidney_model.pkl")
scaler = joblib.load("kidney_scaler.pkl")
columns = joblib.load("kidney_columns.pkl")
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c


# ============================================================
# 4. APPLICATION HEADER
# ============================================================

<<<<<<< HEAD
st.title("🏥Common Illness Disease Prediction System ")

st.write(
    "AI-powered preliminary prediction of common illnesses"
=======
st.title("🩺 Kidney Disease Prediction System")

st.write(
    "Enter patient health details to predict the possibility "
    "of Chronic Kidney Disease."
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
)

st.divider()


# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:

<<<<<<< HEAD
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
=======
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
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
# ============================================================

st.subheader("Patient Information")


<<<<<<< HEAD
# ------------------------------------------------------------
# Fever
# ------------------------------------------------------------

fever = st.number_input(
    "Fever (%)",
    min_value=0.0,
    max_value=100.0,
=======
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
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
    value=0.0,
    step=1.0
)


<<<<<<< HEAD
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
=======
# ============================================================
# 7. PREDICT BUTTON
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
# ============================================================

st.divider()

predict_button = st.button(
<<<<<<< HEAD
    "Predict Disease",
=======
    "🔍 Predict Kidney Disease",
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
    use_container_width=True
)


# ============================================================
<<<<<<< HEAD
# 9. PREDICTION
=======
# 8. PREDICTION
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
# ============================================================

if predict_button:

<<<<<<< HEAD
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
=======
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
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
    # ========================================================

    st.divider()

    st.subheader("Prediction Result")

<<<<<<< HEAD

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
=======
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
>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
        )

    else:

        st.write(
<<<<<<< HEAD
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
=======
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

>>>>>>> a966bea7242938b8c332100cd5d444f566fd1f0c
