import streamlit as st
import pickle
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction", layout="wide", page_icon="❤")

# Custom CSS for the sidebar and main content
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            color: #333;
        }
        .sidebar .sidebar-content .block-container {
            padding: 1rem;
        }
        .main .block-container {
            padding: 2rem;
        }
        .stTextInput>div>div>input {
            background-color: #f9f9f9 !important;
            color: #333 !important;
            border-color: #ccc !important;
        }
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-color: #4CAF50 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the heart disease prediction model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Main content
st.title("Heart Disease Prediction using Machine Learning")

# Display heart image
image = Image.open("Tiny doctors studying huge human heart.jpg")
st.image(image, caption='Heart Disease Prediction', use_column_width=True)

# Create input fields for user data
st.subheader("Input Data")

# Using Streamlit's columns to make the input fields responsive
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=0, step=1)

with col2:
    sex = st.selectbox('Sex', ['Female', 'Male'])

with col3:
    cp = st.selectbox('Chest Pain Types', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])

with col1:
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, step=1)

with col2:
    chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0, step=1)

with col3:
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])

with col1:
    restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])

with col2:
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, step=1)

with col3:
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])

with col1:
    oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, step=0.1)

with col2:
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])

with col3:
    ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, step=1)

with col1:
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

# Predict Heart Disease
if st.button("Predict Heart Disease"):
    # Map input values to numeric values required by the model
    sex_map = {'Female': 0, 'Male': 1}
    cp_map = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3}
    fbs_map = {'False': 0, 'True': 1}
    restecg_map = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
    exang_map = {'No': 0, 'Yes': 1}
    slope_map = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}
    thal_map = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}
    
    sex = sex_map[sex]
    cp = cp_map[cp]
    fbs = fbs_map[fbs]
    restecg = restecg_map[restecg]
    exang = exang_map[exang]
    slope = slope_map[slope]
    thal = thal_map[thal]

    # Predict heart disease using the model
    prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if prediction[0] == 1:
        st.error("The person is predicted to have heart disease.")
    else:
        st.success("The person is predicted to not have heart disease.")