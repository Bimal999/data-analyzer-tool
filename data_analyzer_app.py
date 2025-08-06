import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analyzer Tool", layout="wide")
st.title("📊 Data Analyzer Tool")
st.write("Upload a CSV file to explore your data.")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    st.subheader("Column Information")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Plotting
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.subheader("Choose columns to plot")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if len(numeric_cols) >= 2:
        col1 = st.selectbox("Select X-axis column", numeric_cols)
        col2 = st.selectbox("Select Y-axis column", numeric_cols, index=1)

        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x=col1, y=col2, ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("Not enough numeric columns to plot.")
