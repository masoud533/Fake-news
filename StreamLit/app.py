import streamlit as st

st.title('Fake or Real News Detection with AI!')

text = st.text_area("Enter your news text: ")

btn = st.button("Detect")