import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import pickle
import base64
import matplotlib.pyplot as plt

# Set page title and icon
st.set_page_config(page_title = "CoveClean Innovations", page_icon = "🧹")

#Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["🧹 About Us", "🧽 Services", "🧺 Pricing", "🧼 Reviews", "🧻 Contact Us"])

# setting color theme
custom_theme = f"""
    <style>
        :root {{
            --primaryColor: #9C8777;
            --backgroundColor: #FFE2D3;
            --secondaryBackgroundColor: #E2C3B2;
            --textColor: #543022;
            --font: sans-serif;
        }}
    </style>
"""

st.markdown(custom_theme, unsafe_allow_html=True)

#build homepage
if page == "🧹 About Us":
    st.title("💼 CoveClean Innovations")
    # Audio File 9 to 5
    st.write("🎶: 9 to 5 by Dolly Parton and Kelly Clarkson")
    audio_file_path = "audio/9to5dollypar.mp3" 
    st.audio(audio_file_path, format='audio/mp3', start_time=0)
    st.subheader("Welcome To CoveClean Innovations! Transforming Spaces One Cove At A Time.")
    st.write("Please use the toggle bar on the left hand side of the page to navigate between our services, our pricing, reviews, and contact information.")
    
    # Centered image
    st.image("***insert coveclean innovations logo**** file address****", 
         caption="CoveClean Innovations Logo",
         use_column_width=True,
         output_format="auto",
         width=0.5) 

#build services page
if page == "🧽 Services":
    st.title("🧽 Services")
    st.subheader("Our Services")
    st.write("*** Make colums ** Home cleaning ** corporate cleaning ** list services** or image **")
    st.image("***insert image address link here")
    st.link_button("Click here to learn more", "***link to address of pdf for services sheet", help = "Services", type = 'primary')

#build pricing page
if page == "🧺 Pricing":
    st.title("🧺 Pricing")
    num_cols = df.select_dtypes(include='number').columns.tolist()
    obj_cols = df.select_dtypes(include='object').columns.tolist()
    eda_type = st.multiselect("Pricing")
                
# Build reviews page
if page == "🧼 Reviews":
    st.title("🧼 Reviews")
    st.markdown("Reviews & Recommendations")
   
# Build contact us page
if page == "🧻 Contact Us":
    st.title("🧻 Contact Us")
    st.write("Contact Us!")