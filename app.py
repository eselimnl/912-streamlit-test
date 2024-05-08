import streamlit as st

st.title('My ESU Streamlit app 2')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)
