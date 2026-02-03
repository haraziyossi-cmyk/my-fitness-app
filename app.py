import streamlit as st
import time
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ProFit AI", page_icon="🔥")

st.title("🔥 ProFit: Muscle & Abs")

# תפריט
with st.expander("🥗 תפריט 2000 קלוריות"):
    st.write("חלבון: עוף, טונה, ביצים | פחמימה: אורז, בטטה")

# טיימר
st.header("🏋️ אימון מודרך")
mode = st.selectbox("בחר אימון:", ["ניפוח שריר", "חיטוב וקוביות"])
duration = st.number_input("שניות לתרגיל:", value=45)

if st.button("🚀 התחל טיימר"):
    bar = st.progress(0)
    status = st.empty()
    for i in range(int(duration)):
        time.sleep(1)
        remaining = int(duration) - i - 1
        bar.progress((i + 1) / int(duration))
        status.text(f"זמן נותר: {remaining} שניות")
    
    # הלינק המתוקן עם סיומת mp3
    st.audio("https://www.soundjay.com")
    st.success("סיימת! נוח דקה ועבור לסט הבא.")
    st.balloons()

# מעקב משקל
st.divider()
st.header("📈 מעקב משקל")
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["date", "weight"])

with st.form("progress_form"):
    w = st.number_input("משקל שהרמת היום (קג):", step=0.5)
    submit = st.form_submit_button("שמור התקדמות")
    if submit:
        new_row = pd.DataFrame({"date": [pd.Timestamp.now()], "weight": [w]})
        st.session_state.data = pd.concat([st.session_state.data, new_row])
        st.success("הנתון נשמר!")

if not st.session_state.data.empty:
    fig = px.line(st.session_state.data, x="date", y="weight", title="התקדמות כוח")
    st.plotly_chart(fig)
