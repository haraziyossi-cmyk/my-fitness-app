import streamlit as st

st.set_page_config(page_title="Finan-Tech AI", layout="wide")

st.title("🚀 Finan-Tech AI Navigator")
st.subheader("השוואת מוצרים פיננסיים חכמה")

st.markdown("""
ברוכים הבאים למערכת הניווט הפיננסי המתקדמת. 
כאן תוכלו לקבל ניתוח אובייקטיבי על קרנות פנסיה, גמל והשתלמות.
""")

query = st.text_input("שאל את המערכת (למשל: מי הקרן עם התשואה הגבוהה ביותר?)")

if st.button("נתח נתונים"):
    st.write("המערכת מנתחת נתונים מרשות שוק ההון...")
    st.warning("החיבור ל-API של משרד האוצר יוגדר בשלב הבא.")

st.sidebar.header("בניית פרופיל אישי")
age = st.sidebar.slider("גיל", 18, 70, 30)
risk = st.sidebar.selectbox("רמת סיכון", ["שמרני", "מאוזן", "דינמי"])

if st.sidebar.button("שלח פרטים לסוכן"):
    st.success("הפנייה התקבלה ב-Finan-Tech!")
