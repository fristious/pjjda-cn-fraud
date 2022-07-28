# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:53:02 2022

@author: frist
"""

import streamlit as st
import plotly_express as px
import pickle

def main():
    with open('model.pkl','rb') as file:
        model = pickle.load(file)
        
    st.title('Webpage prediksi bunga iris')
    
    sl = st.number_input(label="Masukkan Sepal Length =", min_value=0.0, max_value=8.0, step=0.1, value=5.2)
    sw = st.number_input(label="Masukkan Sepal Width =", min_value=0.0, max_value=8.0, step=0.1, value=3.2)
    pl = st.number_input(label="Masukkan Petal Length =", min_value=0.0, max_value=8.0, step=0.1, value=1.2)
    pw = st.number_input(label="Masukkan Petal Width =", min_value=0.0, max_value=8.0, step=0.1, value=0.2)
    
if __name__ == "__main__":
    main()
