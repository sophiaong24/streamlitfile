import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
from google.cloud import firestore

db = firestore.Client()
collection = db.collection('texts')



st.set_page_config(page_title="My Recipe Book", page_icon=":tada:", layout="wide")
success=""
chef= ("https://assets1.lottiefiles.com/packages/lf20_nfzjxjbh.json")
cookbook=("https://assets1.lottiefiles.com/packages/lf20_szviypry.json")



def load_lottieurl (url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
    
right_column, left_column = st.columns(2)
with right_column:
 st.title("Welcome to my Recipe Book!")
st.header("You can put all your favorite recipes in here for easy access!")
st.subheader("You can also separate your recipes by 'cooking' or 'baking'")
with left_column:
 st_lottie(cookbook, height=300 )
st_lottie(chef, height=300)


recipe_name = st.text_input("Enter recipe name")
ingredients=st.text_input("Enter ingredients ")
steps=st.text_input("Enter steps")
st.write (recipe_name) 
st.write (ingredients)
st.write  (steps)

if st.button('Done'):
    with st.spinner('Entering inputs'):
        time.sleep(1)
    doc_ref = collection.document()
    doc_ref.set({
        'text': recipe_name
    })
    success = st.success("Success!")

# docs = collection.stream()

# for doc in docs:
#     # Display the data in Streamlit
#     st.write(f'{doc.id} => {doc.to_dict()}')

if recipe_name  or ingredients or steps:
    success.empty()

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)


