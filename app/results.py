# Import Streamlit
import streamlit as st
import numpy as np

def show_results():
    # Page title
    st.title("Results")

    # Option to upload test data or use already uploaded data
    st.write("Upload test data or use already uploaded data:")
    test_data_option = st.radio("Select test data option", ["Upload new test data", "Use already uploaded data"])

    if test_data_option == "Upload new test data":
        test_data = st.file_uploader("Upload your test data", accept_multiple_files=True)
    else:
        st.write("Using already uploaded data")

    # Button to make predictions
    make_predictions_button = st.button("Make Predictions")

    if make_predictions_button:
        # Estimated time and price for predictions
        time = np.random.uniform(0.5, 2.0)
        price = np.random.uniform(1, 5)
        st.write(f"Estimated time for predictions: {time:.2f} hours")
        st.write(f"Estimated price for predictions: ${price:.2f}")

        # Confirmation for predictions
        confirm_predictions = st.button("Confirm and Start Predictions")

        if confirm_predictions:
            st.write("Computing predictions...")
            st.progress(100)
            st.success("Predictions completed!")

            # Option to download predictions
            st.write("Download Predictions:")
            download_button = st.button("Download")
            if download_button:
                # Generate a file with fake predictions and provide a link for download
                with open("predictions.txt", "w") as f:
                    f.write("Fake predictions")
                with open("predictions.txt", "rb") as f:
                    st.download_button("Download", f, file_name="predictions.txt")
