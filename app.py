import streamlit as st

st.title('My ESU Streamlit app 3')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)
