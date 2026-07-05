import streamlit as st

st.set_page_config(page_title="Finan-Tech AI", layout="wide")
st.title("🚀 Finan-Tech AI Navigator")
st.write("ברוכים הבאים למערכת הניווט הפיננסי.")
query = st.text_input("שאל שאלה פיננסית:")
if st.button("נתח"):
    st.write("המערכת מנתחת נתונים...")
