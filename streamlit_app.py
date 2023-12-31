# Import libraries
import streamlit as st

# Import pages
from app.homepage import show_homepage
from app.data_upload import show_data_upload
from app.data_processing import show_data_processing
from app.analysis import show_analysis
from app.machine_learning import show_machine_learning
from app.results import show_results
from app.data_integration import show_data_integration  # Import the new data integration page

# Page configuration
st.set_page_config(
    page_title="Morningside Platform",
    page_icon="🧬",
    layout="wide",
)

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    selected_page = st.radio("Select a page:", ["Homepage", "Data Upload", "Data Processing", "Data Integration", "Analysis", "Machine Learning", "Results"])  # Add the new page to the sidebar

# Display selected page
if selected_page == "Homepage":
    show_homepage()
elif selected_page == "Data Upload":
    show_data_upload()
elif selected_page == "Data Processing":
    show_data_processing()
elif selected_page == "Analysis":
    show_analysis()
elif selected_page == "Machine Learning":
    show_machine_learning()
elif selected_page == "Results":
    show_results()
elif selected_page == "Data Integration":  # Display the new data integration page
    show_data_integration()
