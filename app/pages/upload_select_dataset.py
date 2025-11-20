import streamlit as st
import pandas as pd

def upload_select_dataset():
    uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
    return pd.DataFrame(uploaded_file)
