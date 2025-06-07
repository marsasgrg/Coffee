import streamlit as st
st.markdown("# Customer feedback form\nYour input helps us brew a better experience")

slideris = st.slider("On a scale of 1 to 10 how would you rate our coffee today?", 1, 10, 8)
AB = st.selectbox("What type of service did you experience?", ["In-Store", "Online", "Phone"])

if slideris < 8:
    st.text_input("Name")
    st.text_area("Feedback")
else:
    st.markdown("[Leave a positive response here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")


