import streamlit as st
import pandas as pd

# Load your dataset here
df = pd.read_csv('Admission_Predict_Ver1.1.csv')




# Introduction
st.title(" US Admission Data Analysis")
st.write("<span style='font-size: 24px;'>👋 Hello! We are a fresh graduated students and  excited to present our analysis of the admissions dataset from US universities.</span>", unsafe_allow_html=True)

# Motivation
st.header("Motivation")
st.write("<span style='font-size: 24px;'>🚀 Our motivation for this analysis is to help prospective graduate students make informed decisions when applying to master's programs. We aim to explore the factors that influence admission chances.</span>", unsafe_allow_html=True)

# About the Dataset
st.header("About the Dataset")
st.write("<span style='font-size: 24px;'>📊 The dataset we used for this analysis is sourced from **IEEE Xplore**. It contains information about graduate school admissions, including various factors that influence admission decisions.</span>", unsafe_allow_html=True)

# Data Columns and Meanings
st.header("Data Columns and Meanings")
st.write("<span style='font-size: 24px;'>📝 Here are the columns in the dataset along with their meanings:</span>", unsafe_allow_html=True)

data_info = {
    "Serial No.": "A unique identifier for each data entry.",
    "GRE Score": "The GRE (Graduate Record Examination) score of the candidate.",
    "TOEFL Score": "The TOEFL (Test of English as a Foreign Language) score of the candidate.",
    "University Rating": "The rating of the university/college the candidate is applying to.",
    "SOP": "Statement of Purpose (SOP) rating.",
    "LOR": "Letter of Recommendation (LOR) rating.",
    "CGPA": "The candidate's Cumulative Grade Point Average (CGPA).",
    "Research": "Whether or not the candidate has research experience (0 = No, 1 = Yes).",
    "Chance of Admit": "The probability of the candidate's admission to the program (target variable)."
}

data_info_html = "<ul>"
for col, meaning in data_info.items():
    data_info_html += f"<li><b>{col}:</b> {meaning}</li>"
data_info_html += "</ul>"

st.write(data_info_html, unsafe_allow_html=True)

# Sample Data
st.header("Sample Data")
st.write("<span style='font-size: 24px;'>📄 Here's a sample of the dataset to give you an idea of what it looks like:</span>", unsafe_allow_html=True)
st.write(df.head())
st.write('')
st.write('')
st.write('')
st.write("<span style='font-size: 24px;'>👋 Github repo: https://github.com/Ayten-web/master_admission .</span>", unsafe_allow_html=True)
