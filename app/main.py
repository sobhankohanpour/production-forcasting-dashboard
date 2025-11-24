import os
import sys

import pandas as pd
import streamlit as st

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.plots import scatterplot

save_dir = os.path.join("data") 

# Ensure the folder exists
os.makedirs(save_dir, exist_ok=True)


home, upload_dataset, data_eng_tab, train_ml_model, prediction_tab = st.tabs([
    "🏠 Home", 
    "📁 Select/Upload Dataset", 
    "🛠️ Data Engineering", 
    "🤖 Train ML Model",
    "🔮 Prediction"
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
        # 1️⃣ North Dakota Natural Gas Production
        st.checkbox("North Dakota Natural Gas Production", key="ND_gas_1990_to_present")
        with st.expander("📝 Dataset description"):
            st.markdown("""
            <div style="
                background-color:#FF7043;  
                color:black;               /* text color */
                padding:10px;
                border-radius:8px;
                font-size:14px;
                line-height:1.5;
            ">
            This dataset comes from North Dakota and contains real-world data. 
            It includes monthly values for gas produced, sold, and flared, along with 
            additional measurements specific to the Bakken formation. Because the data reflects
            actual field-level reporting, it is suitable for analytics, forecasting, and operational studies.
            </div>
            """, unsafe_allow_html=True)

        # 2️⃣ North Dakota Cumulative Oil Production by Formation Through 2020
        st.checkbox(
            "North Dakota Cumulative Oil Production by Formation Through 2020", 
            key="ND_cumulative_formation_2020",
        )
        with st.expander("📝 Dataset description"):
            st.markdown("""
            <div style="
                background-color:#FF7043;
                color:black;
                padding:10px;
                border-radius:8px;
                font-size:14px;
                line-height:1.5;
            ">
            This dataset presents cumulative oil production in North Dakota by geological formation through December 2020. 
            Each row represents a specific formation, reporting the total oil produced (in barrels), the percentage contribution of 
            that formation to the overall production, and the number of wells associated with it. The dataset covers major formations 
            such as Bakken, Three Forks, Madison, Red River, and others, as well as minor formations, providing a comprehensive overview of 
            North Dakota’s oil production landscape. It is structured to facilitate comparative analysis across formations, evaluation of 
            production contributions, and assessment of well counts relative to output over time.
            </div>
            """, unsafe_allow_html=True)

        # 3️⃣ North Dakota Historical Monthly Oil Production by County
        st.checkbox(
            "North Dakota Historical Monthly Oil Production by County (April 1951 – August 2025, Excluding Confidential Wells)", 
            key="ND_historical_barrels_of_oil_produced_by_county",
        )
        with st.expander("📝 Dataset description"):
            st.markdown("""
            <div style="
                background-color:#FF7043;
                color:black;
                padding:10px;
                border-radius:8px;
                font-size:14px;
                line-height:1.5;
            ">
            This dataset provides historical monthly oil production data in North Dakota, 
            broken down by county, excluding confidential wells. 
            The data spans from April 1951 to August 2025. Each row corresponds to a specific month, 
            while each column represents a county, reporting the number of barrels of oil produced during 
            that period. Counties included are Adams, Billings, Bottineau, Bowman, Burke, Divide, Dunn, 
            Golden Valley, Hettinger, McHenry, McKenzie, McLean, Mercer, Mountrail, Renville, Slope, 
            Stark, Ward, and Williams. The dataset is structured to facilitate temporal analysis, 
            county-level comparisons, and trend assessment of oil production across North Dakota over time.
            </div>
            """, unsafe_allow_html=True)

        # 4️⃣ North Dakota Historical MCF Gas Produced by County
        st.checkbox(
            "North Dakota Historical MCF Gas Produced by County (January 1990 – August 2025, Excluding Confidential Wells)", 
            key="ND_historical_MCF_gas_produced_by_county",
        )
        with st.expander("📝 Dataset description"):
            st.markdown("""
            <div style="
                background-color:#FF7043;
                color:black;
                padding:10px;
                border-radius:8px;
                font-size:14px;
                line-height:1.5;
            ">
            This dataset provides monthly numerical data for multiple North Dakota counties, 
            including Adams, Billings, Bottineau, Bowman, Burke, Divide, Dunn, Golden Valley, Hettinger, 
            McHenry, McKenzie, McLean, Mercer, Mountrail, Renville, Slope, Stark, Ward, and Williams, 
            spanning from January 1990 to August 2025. Each row corresponds to a specific month, 
            while each column represents a county, reporting the recorded values for that period. 
            The dataset captures quantitative metrics for each county, which could represent population, 
            production, or another county-level measure. 
            It is structured to facilitate temporal analysis, regional comparisons, and trend observation across counties over time.
            </div>
            """, unsafe_allow_html=True)

        
with data_eng_tab:
    st.info("Here, you can visualize and process your selected dataset(s) before training your model.")

with train_ml_model:
    st.info(
        "Here, you can train machine learning models on the selected dataset, " \
        "configure the hyperparameters, and monitor the training process to achieve " \
        "the best performance."
        )

with prediction_tab:
    st.info("Here, you can predict based on the trained model.")
