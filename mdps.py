# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:03:45 2025

@author: KIIT
"""
import numpy
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('trained_model.sav','rb'))
heart_model =  pickle.load(open('heart_disease_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple Diesease Predictive System', ['Diabetes Prediction','Heart Disease Prediction'],icons = ['activity','heart'],default_index =0)
    
if selected =='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('BloodPressure value')
    with col1:      
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis =''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis ='Patient is diabetic'
        else:
            diab_diagnosis ='Patient is diabetic'
        
        
        
    st.success(diab_diagnosis)
    
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2,col3 = st.columns(3)
	
    # age	sex		trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	
    with col1:
         Age = st.text_input('Age of the Person')
    with col2:
        Sex = st.text_input(' sex of Person')
    with col3:
        cp = st.text_input('cp value')
    with col1:
        trestbps = st.text_input('trestbps value')
    with col2:
        chol = st.text_input('chol level')
    with col3:
        fbs = st.text_input('fbs value')
    with col1:
        restecg = st.text_input('restecg value')
    with col2:
        thalach = st.text_input('thalach value')
    with col3:
        exang = st.text_input('exang value')
    with col1:
        oldpeak = st.text_input(' oldpeak value')
    with col2:
       slope = st.text_input('slope value')
    with col3:
        ca = st.text_input('ca value')
    with col1:
        thal = st.text_input('thaL value')
        
    Age = float(Age) if Age else 0.0
    Sex = int(Sex) if Sex else 0
    cp = float(cp) if cp else 0.0
    trestbps = float(trestbps) if trestbps else 0.0
    chol = float(chol) if chol else 0.0
    fbs = int(fbs) if fbs else 0
    restecg = int(restecg) if restecg else 0
    thalach = float(thalach) if thalach else 0.0
    exang = int(exang) if exang else 0
    oldpeak = float(oldpeak) if oldpeak else 0.0
    slope = int(slope) if slope else 0
    ca = int(ca) if ca else 0
    thal = int(thal) if thal else 0

    
    Heart_diagnosis =''
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([[Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0]==1):
            Heart_diagnosis ='Patient have heart disease'
        else:
            Heart_diagnosis ='Patient is good'
    st.success(Heart_diagnosis)
     
 