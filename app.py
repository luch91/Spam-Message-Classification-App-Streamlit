import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open("model.pkl", "rb"))

# create title

st.title("Predict if message is Spam or not")
