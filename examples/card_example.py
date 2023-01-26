import streamlit as st

from streamlit_cardv2.streamlit_cardv2 import card

st.title("Streamlit Card - test")

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="https://placekitten.com/500/500",
    url="https://github.com/gamcoh/st-card",
)

st.write(res)
