# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:40:27 2024

@author: SAIL
"""

import streamlit as st
import  sales_home, sales_univariate, sales_bivariate, sales_mlModels


st.sidebar.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 20px;
    }
    </style>""", unsafe_allow_html=True)
    



# Create a menu
st.sidebar.title("Sales Spotlight")


# Add buttons to navigate between pages
if st.sidebar.button('Home'):
    st.session_state.page = 'sales_home'
if st.sidebar.button('Univariate Statistics'):
    st.session_state.page = 'sales_univariate'
if st.sidebar.button('Bi-Variate Statistics'):
    st.session_state.page = 'sales_bivariate'
if st.sidebar.button('Machine Learning Models'):
    st.session_state.page = 'sales_mlModels'
    
    



# Display the selected page
if 'page' not in st.session_state:
    st.session_state.page = 'sales_home'
if st.session_state.get('page') == 'sales_home':
    sales_home.main()
elif st.session_state.get('page') == 'sales_univariate':
    sales_univariate.main()
elif st.session_state.get('page') == 'sales_bivariate':
    sales_bivariate.main()
elif st.session_state.get('page') == 'sales_mlModels':
    sales_mlModels.main()
