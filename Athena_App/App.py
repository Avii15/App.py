import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to open the camera
def open_camera():
    st.write("Opening Camera...")
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame, channels="RGB", use_column_width=True)
    cap.release()

# Streamlit UI Design
st.set_page_config(page_title="Athena", page_icon="🔍", layout="wide")

# Session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "welcome"

def set_page(page_name):
    st.session_state.page = page_name

# Welcome Page
if st.session_state.page == "welcome":
    st.title("Welcome to Athena")
    st.write("A One-Stop Solution for Security & AI-Powered Analysis.")
    if st.button("Proceed to Login", use_container_width=True):
        set_page("login")

# Login Page
elif st.session_state.page == "login":
    st.title("Login to Athena")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            set_page("dashboard")
        else:
            st.error("Invalid credentials. Try again.")

# Dashboard Page
elif st.session_state.page == "dashboard":
    st.sidebar.title("ATHENA Dashboard")
    st.sidebar.write("Select a feature below:")
    
    feature = st.sidebar.radio("Choose an AI Feature", ["Object Tracking", "Object Detection", "Emotion Recognition", "Threat Detection"])
    
    st.title(f"{feature}")
    st.write("Click below to start camera for this feature.")
    
    if st.button("Open Camera", use_container_width=True):
        open_camera()
