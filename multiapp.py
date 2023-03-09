import pickle
# import sklearn
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models
diabetes_model = pickle.load(open('/Users/darshmac/Documents/Multiple_Disease_ML_Project/saved models/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('/Users/darshmac/Documents/Multiple_Disease_ML_Project/saved models/heart_model.sav','rb'))

parkinson_model = pickle.load(open('/Users/darshmac/Documents/Multiple_Disease_ML_Project/saved models/parkinson_model.sav', 'rb'))

#sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinons Prediction'],
                           default_index = 1)
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Disease Prediction(Females)')
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness(taken from triceps)')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of Person')
    
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating button for prediction
    if st.button('Get Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The Person is Diabatic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
    
    st.success(diab_diagnosis)
    

if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction')
    
if (selected == 'Parkinons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction')