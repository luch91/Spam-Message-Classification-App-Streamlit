import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open("C:\\Users\\user\\Desktop\\Spam Classifier\\Spam-Message-Classification-App-Streamlit\\model.pkl", "rb"))

# create title

st.title("Predict if message is Spam or not")

message = st.text_input("Enter your message")

submit = st.button("Predict")

if submit:
    prediction = model.predict([message])

    print(prediction)
    st.write(prediction)

    if prediction[0] == "spam":
        st.warning("This message is spam")
    else:
        st.success("This message is Legit(HAM)")
        
st.balloons()

