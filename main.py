import streamlit as st
st.markdown("# Customer feedback form\nYour input helps us brew a better experience")
"""
num = 0
if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.button("increase number"):
    st.session_state.stage += 1
    st.write(st.session_state.stage)
else:
    st.write(st.session_state.stage)
st.markdown('## Did you enjoy it?')
if st.button("Yes"):
    st.write("Glad you enjoyed it")
if st.button("No"):
    st.write("We're sorry to hear that")
"""
slideris = st.slider("On a scale of 1 to 10 how would you rate our coffee today?", 1, 10, 5)
AB = st.selectbox("What type of service did you experience?", ["In-Store", "Online", "Phone"])

if slideris < 8:
    st.text_input("What was wrong?")
else:
    st.markdown("[Leave a positive response here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")


