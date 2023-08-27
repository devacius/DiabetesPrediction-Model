# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:05:12 2023

@author: devac
"""

import numpy as np
import pickle 
import streamlit as st

#loaded the saved model
loaded_model = pickle.load(open("D:\downloads\anacondakalund\envs\MachineLearning\trained_model.sav"))


  
def diabetes_prediction(input_data):
    
    input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      print('The person is not diabetic')
    else:
      print('The person is diabetic')
      
def main():
    #giving the title
    st.title('Diabetes Prediction Web App')
    
    #getting the input data from the user
   # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age 
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure value')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age =st.text_input('Age of the person')
    
    diagnosis = ''
    #creating a  function for prediction
    if st.button('Diabetes Test Result'):
        diaganosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
       
    st.success(diagonsis)
    
if__name__=='__main__':
    main()