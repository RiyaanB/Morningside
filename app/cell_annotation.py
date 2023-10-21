# Import Streamlit
import streamlit as st

def show_cell_annotation():
    # Page title
    st.title("Cell Annotation")

    # Instruction image
    st.image("cell_annotation_example.png", caption="Example of cell annotation", use_column_width=True)

    # File uploader
    uploaded_file = st.file_uploader("Upload your image", type="jpg")

    # Display uploaded image
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Perform cell annotation (mock)
        annotate_button = st.button("Annotate Cells")

        if annotate_button:
            st.write("Annotating cells...")
            st.progress(100)
            st.success("Cells annotated!")

            # Display annotated image (mock)
            st.image(uploaded_file, caption="Annotated Image", use_column_width=True)
    else:
        st.write("Please upload an image.")
