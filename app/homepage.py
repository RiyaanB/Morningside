# Import Streamlit
import streamlit as st

def show_homepage():
    # Page title
    st.title("Welcome to the Morningside Platform")

    # Description
    st.write("""
        The Morningside Platform is a comprehensive solution for researchers and scientists working with Omic datasets. 
        Our platform provides tools for data processing, analysis, and machine learning model training, 
        streamlining your workflow and helping you extract meaningful insights from large-scale biological data.
    """)

    # Optional: Add an image or graphic
    # st.image("path/to/image.jpg", caption="Image Caption")
