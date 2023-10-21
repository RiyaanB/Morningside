# Import Streamlit
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from umap import UMAP
import matplotlib.pyplot as plt

def show_data_integration():
    # Page title
    st.title("Data Integration")

    # Human body image map
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image("human_body_image.jpg", width=300)

    # Instructions
    st.write("Click on a body part to view datasets from the literature related to that body part.")

    # Mock interaction (since we can't have clickable regions in Streamlit)
    body_parts = ["Head", "Chest", "Arms", "Legs"]
    selected_body_part = st.selectbox("Select a body part:", body_parts)

    datasets = []
    selected_datasets = []

    # Display datasets for the selected body part
    if selected_body_part == "Head":
        st.write("Datasets for the head:")
        datasets = ["Dataset 1: Brain tissue analysis (GEO12345)", "Dataset 2: Eye tissue analysis (GEO67890)"]
    elif selected_body_part == "Chest":
        st.write("Datasets for the chest:")
        datasets = ["Dataset 1: Heart tissue analysis (GEO11111)", "Dataset 2: Lung tissue analysis (GEO22222)"]
    elif selected_body_part == "Arms":
        st.write("Datasets for the arms:")
        datasets = ["Dataset 3: Muscle tissue analysis (GEO33333)", "Dataset 4: Skin tissue analysis (GEO44444)"]
    elif selected_body_part == "Legs":
        st.write("Datasets for the legs:")
        datasets = ["Dataset 5: Bone tissue analysis (GEO55555)", "Dataset 6: Nerve tissue analysis (GEO66666)"]

    # Option to choose datasets
    selected_datasets = [st.checkbox(dataset) for dataset in datasets]

    # Option to merge with your dataset
    merge_button = st.button("Merge with my dataset")
    if merge_button:
        selected_datasets = [dataset for dataset, selected in zip(datasets, selected_datasets) if selected]
        st.write("Selected datasets:")
        st.write(selected_datasets)
        st.write("Merging datasets...")
        st.progress(100)
        st.success("Datasets merged!")

        # Generate fake counts matrix
        counts_matrix = np.random.randint(1, 1000, size=(100, 5))
        counts_df = pd.DataFrame(counts_matrix, columns=["Gene1", "Gene2", "Gene3", "Gene4", "Gene5"])
        
        # Display counts matrix
        st.write("Counts Matrix:")
        st.dataframe(counts_df)

        # Perform dimensionality reduction using UMAP
        reducer = UMAP(n_components=2)
        embedding = reducer.fit_transform(counts_matrix)
        
        # Display UMAP plot
        st.write("UMAP Plot:")
        fig, ax = plt.subplots()
        scatter = ax.scatter(embedding[:, 0], embedding[:, 1])
        st.pyplot(fig)
