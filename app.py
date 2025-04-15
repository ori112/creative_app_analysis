import streamlit as st
from utils.file_loader import load_inputs
from utils.gemini_handler import analyze_creatives
from config import GEMINI_API_KEY

st.set_page_config(page_title="Creative Analyzer", layout="wide")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Creative Performance Analyzer")

uploaded_csv, uploaded_images = load_inputs()

if uploaded_csv and uploaded_images and st.button("Analyze with Gemini"):
    with st.spinner("Analyzing with Gemini..."):
        result = analyze_creatives(uploaded_csv, uploaded_images, GEMINI_API_KEY)
        st.subheader("Gemini Insights")
        st.text_area("Output", result, height=400)

st.markdown("""
<div class="custom-footer">
    Created by <strong>Ori Alatash</strong> • 
    <a href="mailto:oalatash@gmail.com">oalatash@gmail.com</a>
</div>
""", unsafe_allow_html=True)