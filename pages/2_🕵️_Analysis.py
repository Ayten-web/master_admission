import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import plotly.graph_objects as go
from matplotlib.animation import FuncAnimation




# Load the dataset
df = pd.read_csv('Admission_Predict_Ver1.1.csv')
df = df.drop(['Serial No.'], axis=1)
df = df.rename(columns={'Chance of Admit ': 'Chance of Admit'})
df = df.rename(columns={'LOR ': 'LOR'})  # Correct the column name her
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")




page = st.sidebar.selectbox(  "Select Page",   ["Analysis Results"])
# Analysis Results Page
if page == "Analysis Results":
    st.title("Analysis")



    st.subheader("🤔 What is the average SOP, LOR & University Rating of students who got admitted?")
    st.text("")
    st.text("")

    acceptance_chance = st.slider('''What is the average SOP, LOR & University Rating of students who got admitted?
                                          Select Minimum Acceptance Chance:''', 0.0, 1.0, 0.75)
    # Filter the data based on user input
    filtered_df = df[df["Chance of Admit"] >= acceptance_chance]
    st.write(f"<div style='font-size: 17px;Number of candidates with a chance of admission >= {acceptance_chance}: {len(filtered_df)}<span>", unsafe_allow_html=True)
    st.write("")
    # Create plots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

    # Plot for SOP
    s1 = filtered_df["SOP"].value_counts().sort_index()
    ax1.set_title("SOP of Candidates")
    s1.plot(kind='bar', linestyle='dashed', linewidth=5, ax=ax1)
    ax1.set_xlabel("SOP")
    ax1.set_ylabel("Candidates")
    


    # Plot for LOR
    s2 = filtered_df["LOR"].value_counts().sort_index()
    ax2.set_title("LOR of Candidates")
    s2.plot(kind='bar', linestyle='dashed', linewidth=5, color="green", ax=ax2)
    ax2.set_xlabel("LOR")
    ax2.set_ylabel("Candidates")
    st.pyplot(fig)
    plt.close()

    st.text("")
    st.text("")
    st.text("")
    

    df2 = df[df["Chance of Admit"] > 0.75]
    # Calculate the average ratings
    average_sop_rating = df2['SOP'].mean()
    average_lor_rating = df2['LOR'].mean()
    average_university_rating = df2['University Rating'].mean()

    st.write("Candidates with a 75% or higher acceptance chance:")
    st.write(f"<div style='font-size: 20px;'>Average SOP Rating: {average_sop_rating:.2f} out of 5</div>", unsafe_allow_html=True)
    st.write(f"<div style='font-size: 20px;'>Average LOR Rating: {average_lor_rating:.2f} out of 5</div>", unsafe_allow_html=True)
    st.write(f"<div style='font-size: 20px;'>Average University Rating: {average_university_rating:.2f} out of 5</div>", unsafe_allow_html=True)















    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("🧐 Does the student who is academically good, doing well in GRE and TOEFL?")
    st.text("")

    plt.figure(figsize=(11, 11))
    plt.subplot(2, 2, 1)
    sns.regplot(x='CGPA', y='TOEFL Score', data=df, color='orange')
    plt.title("CGPA vs. TOEFL Score Regression")
    plt.subplot(2, 2, 2)
    sns.regplot(x='CGPA', y='GRE Score', data=df, color='green')
    plt.title("CGPA vs. GRE Score Regression")
    st.pyplot(plt.gcf())  # Pass the current figure
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.write("<span style='font-size: 20px;'>🤓 The Academic toppers are the top scorers in both TOEFL and GRE. </span>", 
            unsafe_allow_html= True)





    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("🤔 Does the Student from top universities are doing research papers?")
    st.text("")

    fig = px.strip(
        df,
        x="CGPA",
        y="Research",
        orientation="h",
        color="University Rating",
        title="Strip Plot: CGPA vs. Research by University Rating",
    )
    fig.update_layout(
        autosize=False,
        width=800,  # Adjust the width as needed
        height=600,  # Adjust the height as needed
    )
    st.plotly_chart(fig)
    st.text("")
    st.text("")
    st.text("")
    st.write('''<span style='font-size: 20px;'>🤓 Mostly the students from top univerties with ratings more than 3 are 
             releasing research papers  and also they are scoring good CGPA(>8).</span>''',unsafe_allow_html= True )





    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("🤔 Does research paper really having a good impact in admission?")
    pie_fig = px.pie(
        df,
        names='Research',
        title='Students Research',
        hole=0.5,
        hover_data=['Research'],
        labels={'0': 'Students with no Research', '1': 'Students who did Research'},
        category_orders={"Research": ["0", "1"]}
    )

    # Create a countplot using Plotly
    research_values = df['Research']
    colorss = ['#374cc4' if research == 0 else '#377814' for research in research_values]

    countplot_fig = px.histogram(
            df,
            
            x='Research',
            title='Students Research',
            color= colorss,
            category_orders={"Research": ["0", "1"]}
    )
    
    countplot_fig.update_traces(marker=dict(line=dict(color='black', width=2)))
    if st.checkbox("Additional Info"):
        research_value = st.selectbox("Select Research Value", ["0", "1"])
        if research_value == "0":
            st.write("Students with Research = 0 havent participate in Research work.")
        elif research_value == "1":
            st.write("Students with Research = 1 have already participated at least in one Research work .")

    st.text("")
    st.text("")
    st.text("")
    st.text("")

    # Display the interactive plots using st.plotly_chart
    st.plotly_chart(pie_fig)
    st.plotly_chart(countplot_fig)
    st.text("")
    st.text("")
    st.text("")




    fig, ax = plt.subplots(figsize=(8, 6))
    research_values = df['Research']
    admit_chances = df['Chance of Admit']
    colors = ['#374cc4' if research == 0 else '#377814' for research in research_values]
    bars = ax.bar(research_values, admit_chances, color=colors)
    ax.set_xlabel("Research")
    ax.set_ylabel("Chance of Admit")
    ax.set_title("Research vs. Chance of Admission")
    st.pyplot(plt.gcf())

    st.text("")
    st.text("")
    st.text("")
    st.write('''<span style='font-size: 20px;'>🤓We can see that 55% Students have done Research.It possible only the better student 
              could get a chance for doing research. Doing research does  add practical knowledge
              and increases the student skill of working with groups or teams. </span>''', unsafe_allow_html= True)









#
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("🤔 Do GRE & TOEFL scores influence the chance of getting admitted?")
    cor = df.corr()['Chance of Admit']
    cor1 = cor.head(2)
    layout = dict(title='Influence on Chance of getting admitted',
                  xaxis=dict(title='Exams'),
                  yaxis=dict(title='Coorelation Value (Out of 1)'),
                  width=500,
                  height=500
                  )
    fig = go.Figure(data=[go.Scatter(
        x=['GRE Score', 'TOEFL Score'],
        y=[cor1[0], cor1[1]],
        mode='markers',
        marker=dict(
            color=[cor1[0] * 100, cor1[1] * 100],
            size=[cor1[0] * 75, cor1[1] * 75],
            showscale=True
        )
    )], layout=layout)
    st.plotly_chart(fig)
    
    st.text("")
    st.text("")
    st.text("")
    st.text("")


    features_to_choose = ['GRE Score', 'TOEFL Score']
    selected_feature = st.selectbox("Select a feature for correlation analysis", features_to_choose)
    #st.write(f'''<span style='font-size: 20px;'>Correlation analysis for {selected_feature} vs. Chance of Admit.
       #     You can also select features bar (*GRE* or *TOELF*) from left **Filter**  for correlation analysis.  <span/>
        #     ''', unsafe_allow_html= True)
    correlation = df.corr()[selected_feature]['Chance of Admit']
    layout = dict(
        title=f'Influence of {selected_feature} on Chance of Getting Admitted',
        xaxis=dict(title=selected_feature),
        yaxis=dict(title='Correlation Value (Out of 1)'),
        width=500,
        height=500
    )
    fig = go.Figure(data=[go.Scatter(
        x=df[selected_feature],
        y=df['Chance of Admit'],
        mode='markers',
        marker=dict(
            color=df[selected_feature],  # Adjust the scaling factor as needed
            size=df[selected_feature] * 0.17,  # Adjust the scaling factor as needed
            showscale=False
        )
    )], layout=layout)
    st.plotly_chart(fig)


    st.write("<span style='font-size: 20px;'>🤓 Here we can see that the chance of admit is highly correlated with GRE and TOEFEL scores. </span>", unsafe_allow_html = True)



    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("🤔 Does the University Rating influence SOP and LOR Rating?")
    plt.figure(figsize=(12, 12))
    plt.subplot(2, 2, 1)
    sns.scatterplot(x='University Rating', y='LOR', data=df, color='Red')  # Corrected column name here
    plt.subplot(2, 2, 2)
    sns.scatterplot(x='University Rating', y='SOP', data=df, color='Blue', marker="^")
    plt.subplot(2, 2, 3)
    sns.scatterplot(data=df, x='SOP', y='LOR', hue='University Rating')  # Corrected column name here
    st.pyplot(plt.gcf())  
    st.text("")
    st.text("")
    st.text("")
    st.write("<span style='font-size: 20px;'>🤓 With increase in ratings of university, the rating of LOR and SOP also increases. <span/>", unsafe_allow_html = True)
