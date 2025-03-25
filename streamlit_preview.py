import pandas as pd
import streamlit as st

st.set_page_config(page_title="Results Preview", page_icon="🧊", layout="wide")

st.header("Preview Data")

# Load datasets
dataset = pd.read_csv("before_training_ready_data.csv", low_memory=False)
llm_dataset = pd.read_excel("output.xlsx")

common_column = "Row Number"

available_columns = llm_dataset[common_column].dropna().unique()
row_number = st.selectbox("Row Number", available_columns)

st.subheader("LLM Output")
filter_llm = llm_dataset[llm_dataset[common_column] == row_number]
for col in ['Scientific Name', 'Drug-Diagnosis Mapping', 'Item FDA Info', 'Item Internet Info', 'Item Statement', 'LLM Explanation', 'LLM Final Decision']:
    if col in filter_llm.columns:
        st.markdown(f"<p style='color:blue; font-weight:bold;'>{col}:</p> <p style='color:black;'>{filter_llm[col].values[0] if not filter_llm.empty else 'N/A'}</p>", unsafe_allow_html=True)

st.header("Original Data")
st.subheader("Important Columns")
filter_dataset = dataset[dataset[common_column] == row_number]

cols = st.columns(3)  # Create three columns for better readability
original_data_columns = ['Claim ID', 'Review Notes', 'Item Name', 'Item Name 2', 'Primary Diagnosis', 'Secondary Diagnosis', 'Amount Requested', 'Quantity Requested', 'Medical info', 'Service', 'Assessment', 'AI Notes', 'Policy_Active_During_Treatment', 'Days Until Expiration', 'Policy Expired', 'Age', "Denial Reason Description", "Final Decision"]

other_orginal_columns = [col for col in dataset.columns if col not in original_data_columns]


for index, col in enumerate(original_data_columns):
    if col in filter_dataset.columns:
        with cols[index % 3]:  # Distribute data across the three columns
            st.markdown(f"<p style='color:green; font-weight:bold;'>{col}:</p> <p style='color:black;'>{filter_dataset[col].values[0] if not filter_dataset.empty else 'N/A'}</p>", unsafe_allow_html=True)

st.info("Note: Final decision 0 indicates claim was approved and 1 indicates denial.")

cols = st.columns(4)
for index, col in enumerate(other_orginal_columns):
    if col in filter_dataset.columns:
        with cols[index % 4]:
            st.markdown(f"<p style='color:green; font-weight:bold;'>{col}:</p> <p style='color:black;'>{filter_dataset[col].values[0] if not filter_dataset.empty else 'N/A'}</p>", unsafe_allow_html=True)