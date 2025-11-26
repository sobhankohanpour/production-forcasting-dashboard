import os
import sys

import pandas as pd
import streamlit as st

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.plots import (
    scatterplot, lineplot, distplot, histplot, kdeplot, ecdfplot, rugplot,
    catplot, stripplot, swarmplot, boxplot, violinplot, pointplot, barplot
)

from strings.strings import (
    WELCOME_MESSAGE, PLATFORM_DESCRIPTION, UPLOAD_INSTRUCTION, WORKFLOW_SUPPORT_MESSAGE,
    UPLOAD_DATASET_INFO, DESC_NATURAL_GAS_PRODUCTION, DESC_CUMULATIVE_OIL_PRODUCTION_2020, 
    DESC_MONTHLY_OIL_PRODUCTION_BY_COUNTY, DESC_MCF_GAS_PRODUCTION_BY_COUNTY,
    NAME_NATURAL_GAS_PRODUCTION, NAME_CUMULATIVE_OIL_PRODUCTION_2020, 
    NAME_MONTHLY_OIL_PRODUCTION_BY_COUNTY, NAME_MCF_GAS_PRODUCTION_BY_COUNTY
    )


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
    st.write(WELCOME_MESSAGE)
    st.write(PLATFORM_DESCRIPTION)
    st.write(UPLOAD_INSTRUCTION)
    st.write(WORKFLOW_SUPPORT_MESSAGE)
    
dataset_1 = False
dataset_2 = False
dataset_3 = False
dataset_4 = False

with upload_dataset:
    st.info(UPLOAD_DATASET_INFO)

    choice = st.radio(
        "Choose one option:",
        ["I want to upload my dataset.", "I want to select from the real-world datasets."]
    )

    if choice == "I want to upload my dataset.":
        st.write("====================================================")
        st.info("You can upload only `.xlsx` files.")
        number_of_user_dataset = 1
        uploaded_file = st.file_uploader("Upload your dataset", type=["xlsx"])
        if uploaded_file:
            df_uploaded_file = pd.read_excel(uploaded_file)
            st.session_state['uploaded_dataset'] = df_uploaded_file
            st.session_state['uploaded_filename'] = uploaded_file.name
            st.dataframe(df_uploaded_file)


    elif choice == "I want to select from the real-world datasets.":
        st.write("====================================================")
        DATASET_NAMES = [
            NAME_NATURAL_GAS_PRODUCTION,
            NAME_CUMULATIVE_OIL_PRODUCTION_2020,
            NAME_MONTHLY_OIL_PRODUCTION_BY_COUNTY,
            NAME_MCF_GAS_PRODUCTION_BY_COUNTY
        ]

        selected_dataset = st.radio("Select a dataset:", DATASET_NAMES)

        dataset_descriptions = {
            NAME_NATURAL_GAS_PRODUCTION: DESC_NATURAL_GAS_PRODUCTION,
            NAME_CUMULATIVE_OIL_PRODUCTION_2020: DESC_CUMULATIVE_OIL_PRODUCTION_2020,
            NAME_MONTHLY_OIL_PRODUCTION_BY_COUNTY: DESC_MONTHLY_OIL_PRODUCTION_BY_COUNTY,
            NAME_MCF_GAS_PRODUCTION_BY_COUNTY: DESC_MCF_GAS_PRODUCTION_BY_COUNTY,
        }

        with st.expander("Dataset Description"):
            st.write(dataset_descriptions[selected_dataset])



def load_default_dataset(name):
    if name == "North Dakota Natural Gas Production":
        return pd.read_excel("data/ND_gas_1990_to_present.xlsx")
    elif name == "North Dakota Cumulative Oil Production by Formation Through 2020":
        return pd.read_excel("data/ND_cumulative_formation_2020.xlsx")
    elif name == "North Dakota Historical Monthly Oil Production by County":
        return pd.read_excel("data/ND_historical_barrels_of_oil_produced_by_county.xlsx")
    elif name == "North Dakota Historical MCF Gas Produced by County":
        return pd.read_excel("data/ND_historical_MCF_gas_produced_by_county.xlsx")
    else:
        return pd.DataFrame()


with data_eng_tab:
    st.info("Here, you can visualize and process your selected dataset before training your model.")

    # Dataset selection
    if choice == "I want to upload my dataset." and 'uploaded_dataset' in st.session_state:
        st.success(f"✅ You selected your uploaded dataset: {st.session_state['uploaded_filename']}")
        df_to_use = st.session_state['uploaded_dataset']

    elif choice == "I want to select from the real-world datasets.":
        st.success(f"🌍 You selected: {selected_dataset}")
        df_to_use = load_default_dataset(selected_dataset)

    else:
        st.warning("⚠️ No dataset selected yet.")
        df_to_use = pd.DataFrame()

    # If dataset is available
    if not df_to_use.empty:
        st.subheader("📊 Dataset Overview")
        st.dataframe(df_to_use.describe())
        st.dataframe(df_to_use.head())

        # Master toggle for visualization
        if st.toggle("Enable Data Visualization"):
            st.markdown("### 🎨 Choose Plot Group")

            # Group selector
            plot_group = st.selectbox(
                "Select a group of plots:",
                ["Distribution Plots", "Categorical Plots", "Relational Plots"]
            )

            df_columns = df_to_use.columns.tolist()

            # --- Distribution Plots ---
            if plot_group == "Distribution Plots":
                with st.expander("Distribution Plot"):
                    x = st.radio("Select column:", df_columns, index=0, key="dist_x")
                    st.info(f"Plotting distribution of **{x}**")
                    distplot(df_to_use, x=x)

                with st.expander("Histogram"):
                    x = st.radio("Select column:", df_columns, index=0, key="hist_x")
                    bins = st.slider("Number of bins", 5, 100, 10, key="hist_bins")
                    st.info(f"Plotting histogram of **{x}** with {bins} bins")
                    histplot(df_to_use, x=x, bins=bins)

                with st.expander("KDE Plot"):
                    x = st.radio("Select column:", df_columns, index=0, key="kde_x")
                    st.info(f"Plotting KDE of **{x}**")
                    kdeplot(df_to_use, x=x)

                with st.expander("ECDF Plot"):
                    x = st.radio("Select column:", df_columns, index=0, key="ecdf_x")
                    st.info(f"Plotting ECDF of **{x}**")
                    ecdfplot(df_to_use, x=x)

                with st.expander("Rug Plot"):
                    x = st.radio("Select column:", df_columns, index=0, key="rug_x")
                    st.info(f"Plotting rug plot of **{x}**")
                    rugplot(df_to_use, x=x)

            # --- Categorical Plots ---
            elif plot_group == "Categorical Plots":
                with st.expander("Cat Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="cat_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="cat_y")
                    st.info(f"Plotting categorical **{y}** vs **{x}**")
                    catplot(df_to_use, x=x, y=y, kind="box")

                with st.expander("Strip Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="strip_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="strip_y")
                    st.info(f"Plotting strip **{y}** vs **{x}**")
                    stripplot(df_to_use, x=x, y=y)

                with st.expander("Swarm Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="swarm_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="swarm_y")
                    st.info(f"Plotting swarm **{y}** vs **{x}**")
                    swarmplot(df_to_use, x=x, y=y)

                with st.expander("Box Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="box_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="box_y")
                    st.info(f"Plotting box **{y}** vs **{x}**")
                    boxplot(df_to_use, x=x, y=y)

                with st.expander("Violin Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="violin_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="violin_y")
                    st.info(f"Plotting violin **{y}** vs **{x}**")
                    violinplot(df_to_use, x=x, y=y)

                with st.expander("Point Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="point_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="point_y")
                    st.info(f"Plotting point **{y}** vs **{x}**")
                    pointplot(df_to_use, x=x, y=y)

                with st.expander("Bar Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="bar_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="bar_y")
                    st.info(f"Plotting bar **{y}** vs **{x}**")
                    barplot(df_to_use, x=x, y=y)

            # --- Relational Plots ---
            elif plot_group == "Relational Plots":
                with st.expander("Scatter Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="scatter_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="scatter_y")
                    st.info(f"Plotting **{y}** vs **{x}**")
                    scatterplot(df_to_use, x=x, y=y)

                with st.expander("Line Plot"):
                    col1, col2 = st.columns(2)
                    with col1:
                        x = st.radio("Select X‑axis column:", df_columns, index=0, key="line_x")
                    with col2:
                        y = st.radio("Select Y‑axis column:", df_columns, index=1, key="line_y")
                    st.info(f"Plotting **{y}** vs **{x}**")
                    lineplot(df_to_use, x=x, y=y)


with train_ml_model:
    st.info(
        "Here, you can train machine learning models on the selected dataset, " \
        "configure the hyperparameters, and monitor the training process to achieve " \
        "the best performance."
        )
    st.success("🚀 Coming Soon...")

with prediction_tab:
    st.info("Here, you can predict based on the trained model.")
    st.success("🚀 Coming Soon...")
