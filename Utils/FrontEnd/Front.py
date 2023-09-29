import streamlit as st

def fmarkdown(size,color,string):
    """Function that allow to create a markdown with any <h></h> and any color"""
    mark = st.markdown(f"<h{size} style='text-align: center; color: {color};'>{string}</h{size}>", unsafe_allow_html=True)
    return