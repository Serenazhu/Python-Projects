import streamlit as st
from PIL import Image

st.header('Serena Website')

p="C:/Users/zulia/Pictures/Rose_bp.jpg"
image = Image.open(p)
st.image(image, caption='Rose')
st.write('Hello, *World!* :sunglasses:')
st.balloons()