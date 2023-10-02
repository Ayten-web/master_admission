import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv('Admission_Predict_Ver1.1.csv')
df = df.drop(['Serial No.'], axis=1)
df = df.rename(columns={'Chance of Admit ': 'Chance of Admit'})
df = df.rename(columns={'LOR ': 'LOR'})  # Correct the column name here

# Set the background image
background_image = '/home/aytan/Desktop/admission/pages/photo-1464618663641-bbdd760ae84a.jpeg'

# Define your Streamlit app content
st.set_page_config(
    page_title="Admission Data Analysis",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set the background image using CSS
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url("{background_image}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)



# Future Work Section
st.header("Future Work 🚀")
st.write("There are several avenues for future work and enhancements to this analysis:")
st.write("- Explore more advanced machine learning models for admission prediction.")
st.write("- Incorporate additional features, such as extracurricular activities or statement of purpose text analysis.")
st.write("- Conduct a deeper analysis of the influence of each feature on admission chances.")
st.write("- Create a predictive model to estimate a candidate's admission probability.")

# Contact Section
st.header("Contact 📧")
st.write("If you have any questions or suggestions, please feel free to reach out:")
st.write("- Email: your.masteradmission@gmail.com 📩")
st.write("- LinkedIn: [ LinkedIn Profile](https://www.linkedin.com/in/masteradmission/) 💼")
st.write("- GitHub: [ GitHub Profile](https://github.com/masteradmission) 🌐")

