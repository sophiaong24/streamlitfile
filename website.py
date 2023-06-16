import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.title ("Welcome to my Recipe Book!")
st.header("You can put all your favorite recipes in here for easy access!")
st.subheader("You can also seperate your recipes by 'cooking' or 'baking'")
lottiefiles = "https://lottiefiles.com/45730-recipes-book-animation"
st.set_page_config (page_title= "Welcome to my Recipe Book")
def load_r = requests.get(url)
 if r.status_code !=200