import streamlit as st

st.title("My web app")

st.header("My custom header")

st.write("learning streamlit for the first time.")

agree = st.checkbox("I agree with Mohit...")

if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"],
)

if genre == "Comedy":
    st.write("You comedy me... Haha.")



    