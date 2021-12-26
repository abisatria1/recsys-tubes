"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.sidebar.title('Sistem Rekomendasi Buku')
st.sidebar.markdown('Aplikasi ini membantu anda dalam menemukan buku yang mirip dengan buku yang kamu sukai, silahkan pilih beberapa buku yang tersedia di sistem kami')
select_box = st.sidebar.selectbox('Masukkan nama buku', [1,2,3,4,5])  

if st.sidebar.button('Rekomendasi') : 
  st.markdown('#### Hasil Rekomendasi')
  col1, col2, col3 = st.columns(3)
  with col1:
      st.markdown('#### Mantap Jiwa')
      st.text('ini description')
  with col2:
      st.markdown('#### Mantap Jiwa')
      st.text('ini description')
  with col3:
      st.markdown('#### Mantap Jiwa')
      st.text('ini description')

# else : 
  # st.markdown('#### Silahkan pilih buku dan klik rekomendasi')
