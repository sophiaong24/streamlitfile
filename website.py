import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Recipe Book", page_icon=":tada:", layout="wide")

st.title("Welcome to my Recipe Book!")
st.header("You can put all your favorite recipes in here for easy access!")
st.subheader("You can also separate your recipes by 'cooking' or 'baking'")
recipe_name:st.text_input("Enter recipe name")
ingredients:st.text_input("Enter ingredients ")
steps:st.text_input("Enter steps")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
 
lottie_coding = load_lottieurl("https://lottiefiles.com/45730-recipes-book-animation")

st_lottie(lottie_coding, height=300)
          