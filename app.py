# Import Required Libraries

import joblib 
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables (for API keys)
load_dotenv()

# Load Models

# Heart Disease model, scaler, and feature columns
heart = {
    "heart_model": joblib.load('./picklefiles/heart_model.pkl'),
    "heart_scaler": joblib.load('./picklefiles/heart_scaler.pkl'),
    "heart_columns": joblib.load('./picklefiles/heart_columns.pkl')
}

# Diabetes model, scaler, and feature columns
diabetes = {
    "diabetes_model": joblib.load('./picklefiles/diabetes_model.pkl'),
    "diabetes_scaler": joblib.load('./picklefiles/diabetes_scaler.pkl'),
    "diabetes_columns": joblib.load('./picklefiles/diabetes_columns.pkl')
}

# kidney model, scaler, and feature columns
kidney = {
    "kidney_model": joblib.load('./picklefiles/kidney_model.pkl'),
    "kidney_scaler": joblib.load('./picklefiles/kidney_scaler.pkl'),
    "kidney_columns": joblib.load('./picklefiles/kidney_columns.pkl')
}

# illness model, scaler, and feature columns
illness = {
    "illness_model": joblib.load('./picklefiles/illness_model.pkl'),
    "illness_scaler": joblib.load('./picklefiles/illness_scaler.pkl'),
    "illness_columns": joblib.load('./picklefiles/illness_columns.pkl')
}

st.title('🤖 AI Powered Health Assistant')
st.divider()

# Sidebar for disease selection and chatbot
with st.sidebar:
     
    st.header("⚕️AI Health Assistant")

    st.write("AI-powered preliminary health likelihood system." \
    "Empowering healthcare with AI — early detection, preventive guidance.")

    st.divider()

    # Dropdown for disease type
    choice_type = st.selectbox(
        "Select Your Disease To Predict : ",
        ["Heart Disease", "Diabetes", "Kidney Disease", "Common Illness"]
    )

    st.divider()

    # Simple chatbot section
    st.header("AI Chatbot")
    user_input = st.text_input("Ask the AI Chatbot:")
    if st.button("Get Response"):
        try:
            model_groq = init_chat_model("groq:llama-3.1-8b-instant")
            response = model_groq.invoke(user_input)
            st.write("Response:", response.content)
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.set_page_config(
    page_title = '🤖AI Powered Health Assistant',
    layout = 'centered'
)

# Heart Disease Prediction Section

if choice_type == "Heart Disease":
    st.subheader('🫀Heart Disease Prediction')
    st.write('Enter patient details below to predict Heart Disease.')

    # Collect patient inputs

    age = st.number_input( 'Age', min_value = 1, max_value = 120, value = 49 )

    sex = st.selectbox( 'Sex', ['M', 'F'])

    chestpaintype = st.selectbox( 'ChestPainType', [ 'ASY', 'ATA', 'NAP', 'TA'] )

    restingbp = st.number_input( 'RestingBP', min_value = 50, max_value = 250, value = 140 )

    cholesterol = st.number_input( 'Cholesterol', min_value = 0, max_value = 700, value = 234 )

    fastingbs = st.selectbox( 'FastingBS', [ 0 , 1] )

    restingecg = st.selectbox( 'RestingECG', ['Normal', 'ST', 'LVH'] )

    maxhr = st.number_input( 'MaxHR', min_value = 50, max_value = 250, value = 140 )

    exerciseangina = st.selectbox( 'ExerciseAngina', ['Y', 'N'] )

    oldpeak = st.number_input( 'Oldpeak', min_value = 0, max_value = 10, value = 1 )

    stslope = st.selectbox( 'ST_Slope', ['Flat', 'Up', 'Down'] )

    # Prediction button

    if st.button('Predict'):
            
        input = pd.DataFrame({
            "Age" : [age],
            "Sex" : [sex],
            "ChestPainType" : [chestpaintype],
            "RestingBP" : [restingbp],
            "Cholesterol" : [cholesterol],
            "FastingBS" : [fastingbs],
            "RestingECG" :[restingecg],
            "MaxHR" : [maxhr],
            "ExerciseAngina" : [exerciseangina],
            "Oldpeak" : [oldpeak],
            "ST_Slope" : [stslope]
        }
        )

        # Encode categorical variables
        input = pd.get_dummies(input).astype(int)
        input = input.reindex(columns=heart['heart_columns'], fill_value=0)

        # Scale numeric features
        numeric_cols = ["Age",	"RestingBP",	"Cholesterol",	"FastingBS",	"MaxHR",	"Oldpeak"]
        input[numeric_cols] = heart['heart_scaler'].transform(input[numeric_cols])

        # Display result
        prediction = heart['heart_model'].predict(input)
        
        if prediction[0] == 1:
            st.error("Heart Disease: Yes")
        else:
            st.success("Heart Disease: No")

        st.divider()

        # Guidance section
        if prediction[0] == 1:
            st.subheader("Guidance")
            if restingbp > 130:
                st.write("High RestingBP — reduce salt and manage stress.")
            if cholesterol > 200:
                st.write("High Cholesterol — eat healthy and exercise.")
            if maxhr < 100:
                st.write("Low MaxHR — improve fitness with safe activity.")
            if age > 45:
                st.write("Age factor — regular heart check‑ups advised.")

# Diabetes Prediction Section

elif choice_type == "Diabetes":
    st.subheader('🩸 Diabetes Prediction')
    st.write("Enter patients details below to predict diabetes.")

    # Collect patient inputs

    pregnancies = st.number_input( "Pregnancies", min_value = 0, max_value = 17, value = 2 )

    glucose = st.number_input( "Glucose", min_value = 40, max_value = 200, value = 148 )

    bloodpressure = st.number_input( "BloodPressure", min_value = 25, max_value = 130, value = 72 )

    skinthickness = st.number_input( "SkinThickness", min_value = 5, max_value = 100, value = 35 )

    insulin = st.number_input( "Insulin", min_value = 10, max_value = 850, value = 257 )

    bmi = st.number_input( "BMI", min_value = 15, max_value = 70, value = 33 )

    diabetespedigreefunction = st.number_input( "Diabetes PedigreeFunction", min_value = 0, max_value = 3, value = 1 )

    age = st.number_input( "Age", min_value = 15, max_value = 81, value = 50 )

    # Prediction button
    if st.button('Predict'):
            input = pd.DataFrame({
                "Pregnancies": [pregnancies],
                "Glucose": [glucose],
                "BloodPressure": [bloodpressure],
                "SkinThickness": [skinthickness],
                "Insulin": [insulin],
                "BMI": [bmi],
                "DiabetesPedigreeFunction": [diabetespedigreefunction],
                "Age": [age]
            })

            # Encode categorical variables
            input = pd.get_dummies(input).astype(int)
            input = input.reindex(columns=diabetes['diabetes_columns'], fill_value=0)

            # Scale numeric features
            numeric_cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",	"BMI",	"DiabetesPedigreeFunction",	"Age"]
            input[numeric_cols] = diabetes['diabetes_scaler'].transform(input[numeric_cols])

            # Display Prediction
            predicted = diabetes['diabetes_model'].predict(input)
            if predicted[0] == 0:
                st.success("The model predicts a low risk of diabetes.")  
            else:
                st.error("The model predicts a high risk of diabetes.")

            st.divider()

            # Guidance section
            if predicted[0] == 1:
                st.subheader("Guidance")
                if glucose > 140:
                    st.write("High Glucose: Reduce sugar and monitor regularly")
                if bmi > 30:
                    st.write("High BMI: Focus on diet and exercise.")
                if bloodpressure > 120:
                    st.write("High Blood Pressure: Limit salt and manage stress.")
                if age > 45:
                    st.write("Age Factor: Schedule regular health check‑ups.")

# Kidney Disease Prediction Section

elif choice_type == "Kidney Disease":
    st.subheader("🏥 Kidney Disease Prediction System")

    st.write("Enter patient health details to predict Chronic Kidney Disease.")

    # Collect patient inputs

    age = st.number_input( "Age", min_value=0, max_value=120, value=71)

    creatinine = st.number_input( "Creatinine Level", min_value=0.0, max_value=5.0, value=0.3)

    bun = st.number_input( "BUN Level", min_value=3, max_value=70, value=41)

    diabetes = st.selectbox( "Do you have Diabetes?", ["No", "Yes"] )

    diabetes_value = 1 if diabetes == "Yes" else 0

    hypertension = st.selectbox( "Do you have Hypertension?", ["No", "Yes"] )

    hypertension_value = 1 if hypertension == "Yes" else 0

    gfr = st.number_input( "GFR", min_value=3, max_value=130, value=47)

    urine_output = st.number_input( "Urine Output", min_value=100, max_value=3000, value=1622)

    # Prediction button

    if st.button("Predict"):

        input = pd.DataFrame({
            "Age": [age],
            "Creatinine_Level": [creatinine],
            "BUN": [bun],
            "Diabetes": [diabetes_value],
            "Hypertension": [hypertension_value],
            "GFR": [gfr],
            "Urine_Output": [urine_output]
        })

        # Encode categorical variables
        input = pd.get_dummies(input).astype(int)
        input = input.reindex(columns=kidney['kidney_columns'], fill_value=0)

        # Scale numeric features
        input = kidney['kidney_scaler'].transform(input)

        prediction = kidney['kidney_model'].predict(input)[0]

        # Display prediction
        if prediction == 1:
            st.error("CKD Detected")
        else:
            st.success("Normal - No CKD Detected")

        # Guidance section
        if prediction == 1:
            st.subheader("Guidance")
            st.write("Consult a healthcare professional for proper kidney evaluation.")
            st.write("Follow appropriate hydration advice from your healthcare provider.")
            st.write("Keep blood sugar under control if you have diabetes.")
            st.write("Monitor and manage your blood pressure regularly.")

# Common Illness Prediction Section
elif choice_type == "Common Illness":

    st.subheader("🤒Common Illness Disease Prediction")
    st.write("Enter patient health details.")

    # Collect patient inputs

    fever = st.number_input( "Fever (°F)", min_value=90.0, max_value=110.0, value=98.10, step=0.1)

    headache = st.number_input( "Headache Severity (0–10)", min_value=0.0, max_value=10.0, value= 8.7, step=0.1)

    cough = st.number_input( "Cough Severity (0–10)", min_value=0.0, max_value=10.0, value= 5.88, step=0.1)

    fatigue = st.number_input("Fatigue Severity (0–10)", min_value=0.0, max_value=10.0, value= 5.42, step=0.1)

    body_pain = st.number_input( "Body Pain Severity (0–10)", min_value=0.0, max_value=10.0, value= 2.21, step=0.1)

    if st.button("Predict "):
        input = pd.DataFrame(
                {
                    "Fever": [fever],
                    "Headache": [headache],
                    "Cough": [cough],
                    "Fatigue": [fatigue],
                    "Body_Pain": [body_pain]
                }
            )
         
        # Match Index
        input = input.reindex(columns=illness['illness_columns'], fill_value=0)
        
        # Scale numeric features
        input = illness['illness_scaler'].transform(input)

        # Display prediction
        prediction = illness['illness_model'].predict(input)

        st.success(f"Predicted Disease: {prediction}")

        st.subheader("General Health Guidance")
        st.write("Stay hydrated and get adequate rest.")
        st.write("Monitor your symptoms regularly.")
        st.write("Consult a qualified healthcare professional for proper evaluation.")
        st.write("Do not start or stop medication without professional medical advice.")