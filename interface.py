import streamlit as st
def generate_response(user_input):
    st="I remember Sara you told me about yesterday. Where she is going"
    return st
def generate_response2(user_input):
    st="but you told me recently that she works as a doctor"
    return st
def main():


    st.markdown('<h1 style="color: #DA4545;">Welcome to CogniMemora Ally : Weaving memories together!</h1>', unsafe_allow_html=True)

    user_input = st.text_input("You:", "Type your response here")

    
    st.text_area("Chatbot:", generate_response(user_input))
    user_input2= st.text_input("You:")
    st.text_area("Chatbot:",generate_response2(user_input2))

if __name__ == "__main__":
    main()