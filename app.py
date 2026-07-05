import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Finan-Tech XML", layout="wide")
st.title("📊 מערכת השוואת מוצרים (XML)")

tab1, tab2, tab3 = st.tabs(["פנסיה", "גמל", "ביטוח"])

def show_xml_tab(file_name, tab_name):
    if os.path.exists(file_name):
        try:
            # קריאת קובץ XML ישירות לטבלה
            df = pd.read_xml(file_name)
            st.write(f"### נתוני {tab_name}")
            st.dataframe(df, use_container_width=True)
        except Exception as e:
            st.error(f"שגיאה בקריאת ה-XML ב-{file_name}: {e}")
    else:
        st.error(f"הקובץ {file_name} לא נמצא!")

with tab1:
    show_xml_tab("pension.xml", "פנסיה")
with tab2:
    show_xml_tab("gemel.xml", "גמל")
with tab3:
    show_xml_tab("bituach.xml", "ביטוח")
