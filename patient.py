import streamlit as st

def app2():

        st.title('Welcome to CogniMemora')
        st.title("Enter Patient's Details")
        Name = st.text_input("Enter Patient's Name")
        Age = st.text_input("Enter Patient's Age")
        Gender = st.selectbox('Male/Female/Other',['Male','Female','Other'])

app2()
