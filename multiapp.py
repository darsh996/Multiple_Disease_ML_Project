import pickle
import sklearn
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models
diabetes_model = pickle.load(open('/Users/darshmac/Documents/Multiple_Disease_ML_Project/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('/Users/darshmac/Documents/Multiple_Disease_ML_Project/heart_model.sav','rb'))

parkinson_model = pickle.load(open('/Users/darshmac/Documents/Multiple_Disease_ML_Project/parkinson_model.sav', 'rb'))

#sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System using ML',
                           ['Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Parkinson Prediction'],
                           default_index = 1)  
    

if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction')
    
    age = st.number_input('Age of Patient in years',max_value=100)
    sex = st.number_input('Sex(1= Male/0 = Female)',min_value=0)
    cp = st.number_input('Chest Pain Type',min_value=0)
    trestbps = st.number_input('Resting blood pressure (in mm Hg on admission to the hospital)',min_value=0)
    chol = st.number_input('Serum cholesterol in mg/dl',min_value=0)
    fbs = st.number_input('Fasting Blood Sugar in mg/dl',min_value=0)
    restecg = st.number_input('Rest ECG',min_value=0)
    thalach = st.number_input('Maximum Heart Rate',min_value=0)
    exang = st.number_input('Exercise-induced angina (1 = True/0 = False)',min_value=0)
    oldpeak = st.number_input('ST depression induced by exercise relative to rest',min_value=0)
    slope = st.number_input('Slope of the peak exercise ST segment',min_value=0)
    ca = st.number_input('Number of major vessels (0-3) colored by fluoroscopy',max_value=1)
    thal = st.number_input('Thal (0 = normal; 1 = fixed defect;2 = reversible defect)',min_value=0)
    
    heart_diag = ''
    
    if st.button('Get Result'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,
        chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0] == 1):
            heart_diag = 'Person have heart problem'
        else:
            heart_diag = 'Person is healthy'   

    st.success(heart_diag)
    
    
if (selected == 'Parkinson Prediction'):
    
    #page title
    st.title('Parkinson Prediction')
    
    MDVP1 = st.number_input('Enter Average vocal fundamental frequency Fo(Hz)',min_value=0)
    MDVP2 = st.number_input('Enter Maximum vocal fundamental frequency Fhi(Hz)',min_value=0)
    MDVP3 = st.number_input('Enter Minimum vocal fundamental frequency Flo(Hz)',min_value=0)
    MDVP4 = st.number_input('Enter Several measures of variation in fundamental frequency Jitter(i)',min_value=0)
    MDVP5 = st.number_input('Enter Several measures of variation in fundamental frequency Jitter(Abs)',min_value=0)
    MDVP6 = st.number_input('Enter Several measures of variation in fundamental frequency RAP',min_value=0)
    MDVP7 = st.number_input('Enter Several measures of variation in fundamental frequency PPQ',min_value=0)
    Jitter = st.number_input('Enter Several measures of variation in fundamental frequency DDP',min_value=0)
    MDVP8 = st.number_input('Enter Several measures of variation in fundamental frequency Shimmer',min_value=0)
    MDVP9 = st.number_input('Enter Several measures of variation in amplitude Shimmer(dB)',min_value=0)
    Shimmer1 = st.number_input('Enter Several measures of variation in amplitude APQ3',min_value=0)
    Shimmer2 = st.number_input('Enter Several measures of variation in amplitude APQ5',min_value=0)
    MDVP10 = st.number_input('Enter Several measures of variation in amplitude APQ',min_value=0)
    Shimmer3 = st.number_input('Enter Several measures of variation in amplitude DDA',min_value=0)
    NHR = st.number_input('Enter measures of the ratio of noise to tonal components in the voice(NHR)',min_value=0)
    HNR = st.number_input('Enter measures of the ratio of noise to tonal components in the voice(HNR)',min_value=0)
    RPDE = st.number_input('Enter nonlinear dynamical complexity measures(RDPE)',min_value=0)
    DFA = st.number_input('Enter Signal fractal scaling exponent',min_value=0)
    spread1 = st.number_input('Enter nonlinear measures of fundamental frequency variation(spread1)',min_value=0)
    spread2 = st.number_input('Enter nonlinear measures of fundamental frequency variation(spread2)',min_value=0)
    D2 = st.number_input('Enter nonlinear dynamical complexity measures(D2)',min_value=0)
    PPE = st.number_input('Enter nonlinear measures of fundamental frequency variation(PPE)',min_value=0)
    
    park_diagnose = ''
    
    if st.button('Get Result'):
        park_prediction = parkinson_model.predict([[MDVP1,MDVP2,MDVP3,MDVP4,MDVP5,MDVP6,MDVP7,Jitter,MDVP8,MDVP9,Shimmer1,Shimmer2,MDVP10,Shimmer3,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if(park_prediction[0] == 1):
            park_diagnose = 'Person have Parkinson problem'
        else:
            park_diagnose = 'Person is healthy'   

    st.success(park_diagnose)


#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Disease Prediction(Females)')
    
    #columns for input fields
    # col1,col2,col3 = st.columns(3)
    
    # with col1:
    Pregnancies = st.number_input('Number of Pregnancies',min_value=0)
    # with col2:
    Glucose = st.number_input('Glucose Level',min_value=0)
    # with col3:
    BloodPressure = st.number_input('Blood Pressure Value',min_value=0)
    # with col1:
    SkinThickness = st.number_input('Skin Thickness(taken from triceps)',min_value=0)
    # with col2:
    Insulin = st.number_input('Insulin Level',min_value=0)
    # with col3:
    BMI = st.number_input('BMI Value',min_value=0)
    # with col1:
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value',min_value=0)
    # with col2:
    Age = st.number_input('Age of Person',min_value=0)
    
    
     #code for prediction
    diab_diagnosis = ''
    
    #creating button for prediction
    if st.button('Get Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diab_prediction[0] == 0):
            diab_diagnosis = 'The Person is Not Diabatic'
        else:
            diab_diagnosis = 'The Person is Diabetic'
    
    st.success(diab_diagnosis)