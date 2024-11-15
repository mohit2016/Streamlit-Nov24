import streamlit as st

st.title("Basic Calculator!")

def square(x):
    return x*x 



number = st.number_input("Insert a number")


if st.button("Get square"):
    res = square(number)
    st.header(res)