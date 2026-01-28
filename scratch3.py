# This is the beginning of the actual code

# reviews.query("App in @apps.App", inplace=True)

# # 1
# valid_apps = apps["Apps"]

# reviews.query("App in @valid_apps", inplace=True)

# # 2

# reviews = reviews.loc[reviews["App"].isin(valid_apps)]

# # 3 

# reviews = reviews[reviews["App"].isin(valid_apps)]


# apps = apps.join(aggregated_reviews, on="App", how="left")

# apps = apps.merge(aggregated_reviews, on="App", how="left")

# This is code relevant to day 02 ^^^

import subprocess

file = "C:/Users/4255277/UWC/CSS 2026/day 03/data_pipeline_streamlit/data_pipeline_streamlit/app.py"

# file = "C:/Users/4255277/UWC/CSS 2026/day 03/data_pipeline_streamlit/data_pipeline_streamlit/pipeline_functions.py"
# file = "C:/Users/4255277/UWC/CSS 2026/day 03/data_pipeline_streamlit/data_pipeline_streamlit/app.py"
# file = "C:/Users/4255277/UWC/CSS 2026/day 03/data_pipeline_streamlit/data_pipeline_streamlit/pipeline_module.py"

import streamlit as st

st.write("Hello, World!")

st.write("CSS 2026:")

st.write("day 03")

number = st.slider("Pick a number", 1, 100)

st.write("You picked: ", number)
