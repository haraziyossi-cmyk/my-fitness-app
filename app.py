import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finan-Tech Comparison", layout="wide")
st.title("📊 מערכת השוואת מוצרים פיננסיים")

# יצירת לשוניות לכל תחום
tab1, tab2, tab3 = st.tabs(["פנסיה", "גמל", "ביטוח"])

# פונקציית טעינה - שימוש ב-encoding שמתאים לעברית ובשמות הקבצים המדויקים
def load_and_show(file_name, tab_name):
    try:
        # בגלל שהקבצים בעברית, לעיתים צריך encoding='cp1255'
        df = pd.read_csv(file_name, encoding='cp1255') 
        st.write(f"נתוני {tab_name} מעודכנים:")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"לא ניתן להציג נתוני {tab_name}: {e}")

with tab1:
    load_and_show("נתוני פנסיה נט", "פנסיה")
with tab2:
    load_and_show("נתוני גמל נט", "גמל")
with tab3:
    load_and_show("נתוני ביטוח נט", "ביטוח")
