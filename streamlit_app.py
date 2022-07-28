# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:53:02 2022

@author: frist
"""

import streamlit as st
import plotly_express as px
import joblib

def main():
    with open('model.pkl','rb') as file:
        model = joblib.load(file)
        
    st.title('Prediksi Kesalahan HS Code pada Pemberitahuan CN')
    st.subheader('Silahkan pilih file XML yang akan diuji (.xml/.txt)')
    fl = st.file_uploader('Upload a file')
    st.subheader('Atau masukan variable secara manual')
    sid = st.text_input("NPWP PJT")
    gd = st.text_input("Kode gudang")
    ng = st.text_input("Kode negara")
    jb = st.number_input("Jumlah barang", 0, 100)
    jid = st.selectbox('Pilih jenis ID', ['0', '1','2','3','4','5','9'])
    nid = st.text_input("Nomor ID")
    cif = st.number_input("CIF barang")
    net = st.number_input("Netto barang")
    np = st.text_input("Nama pengirim")
    
if __name__ == "__main__":
    main()
