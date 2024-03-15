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

# Build homepage
if page == "🧹 About Us":
    st.title("🧹 About Us:")
    st.subheader("CoveClean Innovations:")
    
    st.write("Transforming spaces one cove at a time!")
    st.write("Please use the toggle bar on the left hand side of the page to navigate between our services, pricing, reviews, and contact information.")
    
    # Define the file path to your logo image
    logo_path = "coveclean_innovations_logo.png"

    # Display the image
    st.image(logo_path, 
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