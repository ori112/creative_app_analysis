import streamlit as st

def load_inputs():
    st.markdown("### 📊 Upload the performance data CSV")
    st.markdown("###### load your csv, make sure that you have a column listing the creatives for each record, for exmaple, creative_1")
    csv_file = st.file_uploader("Upload CSV with performance data", type="csv")
    st.divider()
    st.markdown("### 🖼️ Upload the creative images used in campaigns")
    st.markdown("###### name your creatives in the same manner in your CSV file, creative_1 creative_2 and so on")
    image_files = st.file_uploader("Upload creative images", type=["png", "jpg"], accept_multiple_files=True)

    if csv_file and image_files:
        return csv_file, image_files
    return None, None
