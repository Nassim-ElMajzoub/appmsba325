# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/167VVpxoV61CagScKp0xZKRx4O7AV5x_P
"""

pip install streamlit

!pip install pyngrok

!ngrok authtoken 2nhzDXWq914212T0rp1WK5ei38D_GGwpYz7A8BtZvH4xALpe

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# 
# # Set the page configuration with a new title and icon
# st.set_page_config(page_title="My Data Dashboard", page_icon="📊", layout="wide")
# 
# st.title("MSBA325 Assignment #2 - Data Visualizing in Streamlit")
# st.subheader("Nassim El Majzoub Dit Mola")
# st.subheader("ID: 202570054")
# 
# 
# # displaced heat map
# df3 = pd.read_csv("https://linked.aub.edu.lb/pkgcube/data/ad5a09f06826cfd4678d2c961127f6b2_20241020_010926.csv")
# 
# # Find the index of the row with the maximum 'Number of People Displaced' and remove since it's an outlier
# max_displaced_index = df3['Number of People Displaced'].idxmax()
# df3 = df3.drop(max_displaced_index)
# 
# # Create a slider for filtering 'Number of People Displaced'
# min_displaced, max_displaced = st.slider(
#     'Select the range of displaced people to highlight on the map:',
#     min_value=int(df3['Number of People Displaced'].min()),
#     max_value=int(df3['Number of People Displaced'].max()),
#     value=(int(df3['Number of People Displaced'].min()), int(df3['Number of People Displaced'].max()))
# )
# 
# # Filter the data based on the slider's range
# filtered_df = df3[(df3['Number of People Displaced'] >= min_displaced) &
#                   (df3['Number of People Displaced'] <= max_displaced)]
# 
# # Create the heatmap using Plotly Express
# fig3 = px.density_mapbox(
#     filtered_df,
#     lat='Latitude',
#     lon='Longitude',
#     z='Number of People Displaced',
#     radius=10,  # Adjust the radius to control the smoothness of the heatmap
#     center=dict(lat=33.8547, lon=35.8623),  # Optionally set the center of the map
#     zoom=7,  # Adjust the zoom level for the map
#     mapbox_style="stamen-terrain"  # You can change this to another map style like 'carto-positron'
# )
# 
# # Update the layout of the map
# fig3.update_layout(
#     title='Heatmap of Displaced People',
#     mapbox_style="open-street-map"  # You can also use 'carto-darkmatter', 'stamen-terrain', etc.
# )
# 
# # Show the heatmap in Streamlit
# st.plotly_chart(fig3)
# 
# 
# 
# 
# # pie chart of airports
# df4 = pd.read_csv("https://linked.aub.edu.lb/pkgcube/data/7fc85a3bdf8cd2306d4b77c32e8fd07e_20241020_015040.csv")
# 
# fig4 = px.pie(df4, names='Type', title='Types of Airports in Lebanon',
#              hole=0.3,  # Optional: to create a donut chart, adjust the hole size (set to 0 for a full pie)
#              )
# 
# # Update layout for percentage display
# fig4.update_traces(textinfo='percent+label')
# 
# # Display the Plotly figure in Streamlit
# st.plotly_chart(fig4)

from pyngrok import ngrok
import os

# Run Streamlit app in the background
os.system('streamlit run app.py &')

# Open ngrok tunnel to port 8501
public_url = ngrok.connect(8501)
print(f'Public URL: {public_url}')