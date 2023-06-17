# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:29:57 2023

@author: Mounika
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open("C:/Users/Mounika/Downloads/trained_model.sav","rb"))

def spam_prediction(input_data):
    input_mail = ["ham","Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."]
    input_data_features = feature_extraction.transform(input_mail)
    prediction = model.predict(input_data_features)
    print(prediction)
    if (prediction[0]==1):
        print('Ham mail')
    else:
        print('Spam mail')
        
        
def main():
    st.title('Spam detection')
    v1 = st.text_input('Number of v1')
    v2 = st.text_input('Name of v2')
    
    diagnosis=""
    
    if st.button("Spam Detection Result"):
        diagnosis=spam_detection('v1','v2')
    
    st.success(diagnosis)
    


if __name__=='__main__':
    main()
