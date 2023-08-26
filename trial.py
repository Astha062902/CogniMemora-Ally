import streamlit as st
import patient


def app():
    st.markdown('<h1 style="color: #DA4545;">Welcome to CogniMemora Ally : Weaving memories together!</h1>', unsafe_allow_html=True)


    choice = st.selectbox('Login/Signup', ['Login','Sign Up'])
    if choice == "Login":
        email= st.text_input('Email Address')
        password= st.text_input('Password',type='password')

        st.button('Login')


    else:
        email= st.text_input('Email Address')
        password = st.text_input('Password', type = 'password')

        username = st.text_input('Enter your unique username')

        st.button('Create my account',on_click=patient.app2)

app()
    