# Import Streamlit
import streamlit as st

def show_data_upload():
    # Page title
    st.title("Data Upload")

    # File uploader
    uploaded_files = st.file_uploader("Upload your FastQ files", type="fastq", accept_multiple_files=True)

    # Display list of uploaded files
    if uploaded_files:
        st.write("Uploaded files:")
        for uploaded_file in uploaded_files:
            st.write(uploaded_file.name)
    else:
        st.write("No files uploaded yet.")
