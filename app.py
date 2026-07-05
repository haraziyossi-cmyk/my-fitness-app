import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finan-Tech Comparison", layout="wide")
st.title("📊 מערכת השוואת מוצרים פיננסיים")

# יצירת לשוניות
tab1, tab2, tab3 = st.tabs(["פנסיה", "גמל", "ביטוח"])

def load_data(file_name):
    if file_name.endswith('.csv'):
        return pd.read_csv(file_name, encoding='cp1255')
    else:
        return pd.read_excel(file_name)

def show_tab(file_name, tab_name):
    try:
        df = load_data(file_name)
        st.write(f"### נתוני {tab_name}")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"שגיאה בטעינת {tab_name}: {e}. וודא ששם הקובץ ב-GitHub תואם לקוד.")

with tab1:
    show_tab("pension.xlsx", "פנסיה")
with tab2:
    show_tab("gemel.xlsx", "גמל")
with tab3:
    show_tab("bituach.xlsx", "ביטוח")
