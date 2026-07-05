import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finan-Tech Data", layout="wide")
st.title("📊 גמל נט - נתונים בזמן אמת")

# הקישור לקובץ האקסל של גמל נט (דוגמה)
URL = "https://data.gov.il/api/3/action/datastore_search?resource_id=53282297-b2f5-4672-9b2f-2879c3558c42&limit=50"

@st.cache_data
def load_data():
    # פונקציה לטעינת נתונים
    df = pd.read_json(URL)
    return df

st.write("טוען נתונים מרשות שוק ההון...")
try:
    df = load_data()
    st.dataframe(df)
except Exception as e:
    st.error(f"שגיאה בטעינת הנתונים: {e}")
