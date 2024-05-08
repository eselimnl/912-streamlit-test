import streamlit as st
# GA
import pathlib
from bs4 import BeautifulSoup
import logging
import shutil

st.title('My ESU Streamlit app 2')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-D39YXHSX0V"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-D39YXHSX0V
        </script>
    """, unsafe_allow_html=True)