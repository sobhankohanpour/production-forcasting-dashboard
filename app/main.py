import os
import pandas as pd
import streamlit as st

save_dir = os.path.join("data") 

# Ensure the folder exists
os.makedirs(save_dir, exist_ok=True)

home, upload_dataset, preprocessing_tab, train_ml_model, prediction_tab = st.tabs([
    "🏠 Home", 
    "📁 Select/Upload Dataset", 
    "🛠️ Preprocessing", 
    "🤖 Train ML Model",
    "Prediction"
])

with home:
    st.title("Welcome to Well Production Forecasting Dashboard 🛢️📈")
    st.write(
        "Welcome to the Well Production Forecasting Dashboard — " \
        "your smart companion for data-driven petroleum engineering."
        )
    st.write(
        "This platform leverages advanced machine learning techniques " \
        "to predict oil and gas production rates with high accuracy."
        )
    st.write(
        "Users can upload their own well datasets, allowing the system to " \
        "train custom models tailored to their field conditions and generate precise, scenario-specific forecasts."
        )
    st.write(
        "Whether you're optimizing field development, monitoring reservoir performance, or " \
        "planning future operations, this dashboard provides actionable insights, intuitive " \
        "visualizations, and AI-powered predictions designed for real-world petroleum engineering workflows."
        )
with upload_dataset:
    st.info(
        """
        You can select from the default datasets included in the project,
        or upload your own custom datasets to use with the models.
        """
    )
    if st.toggle("I want to upload my dataset."):
        st.info(
            """
            You can upload only `.xlsx` files.  
            """
        )
        number_of_user_dataset = st.slider(
            "Number of dataset(s)", min_value=1, max_value=50, value=1
        )
        st.write(f"You must upload {number_of_user_dataset} dataset(s).")

        uploaded_files = []
        for i in range(number_of_user_dataset):
            uploaded_file = st.file_uploader(
                f"Upload dataset #{i+1}", type=["xlsx"], key=f"dataset_{i}"
            )
            if uploaded_file:
                uploaded_file.seek(0)  # reset file pointer
                df_uploaded_file = pd.read_excel(uploaded_file)
                st.dataframe(df_uploaded_file)

                # Save with original name
                save_path = os.path.join(save_dir, uploaded_file.name)
                df_uploaded_file.to_excel(save_path, index=False)
                st.success(f"Dataset #{i+1} saved.")

    if st.toggle("I want to select from the real-word datasets."):
        st.checkbox(
            "North Dakota Natural Gas Production", 
            help="This dataset comes from North Dakota and contains real-world data. " \
            "It includes monthly values for gas produced, sold, and flared, along with " \
            "additional measurements specific to the Bakken formation. Because the data reflects" \
            " actual field-level reporting, it is suitable for analytics, forecasting, and operational studies.",
            key="nd_dataset",
            )
        

with preprocessing_tab:
    st.info("Here, you can process the dataset before training your model on it.")

with train_ml_model:
    st.info(
        "Here, you can train machine learning models on the selected dataset, " \
        "configure the hyperparameters, and monitor the training process to achieve " \
        "the best performance."
        )

with prediction_tab:
    st.info("Here, you can predict based on the trained model.")
