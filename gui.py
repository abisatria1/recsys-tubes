"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

select_box = st.selectbox('Coba selectbox', [1,2,3,4,5])  

if st.button('Recommend') : 
  print('mantap')
