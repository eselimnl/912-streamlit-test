import streamlit as st
# GA
import pathlib
from bs4 import BeautifulSoup
import logging
import shutil

st.title('My ESU Streamlit app 2')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)

import streamlit.components.v1 as components

google_analytics_js = """
<script>
function loadScript(url) {       
    return new Promise(function(resolve, reject) {
        // Add the script to the main page, not the component iframe
        const doc = window.parent.document;
        var head = doc.getElementsByTagName('head')[0];
        var script = doc.createElement('script');
        script.type = 'text/javascript';
        script.src = url;
        script.async = true;
        script.onload = resolve;
        head.appendChild(script);
    });
}

loadScript('https://www.googletagmanager.com/gtag/js?id=G-D39YXHSX0V').then(() => {
    // Initialize Google Analytics
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-D39YXHSX0V');
});
</script>
"""

components.html(
    google_analytics_js,
    height=0,
    width=0
)