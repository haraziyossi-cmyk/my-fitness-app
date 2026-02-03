import streamlit as st
import time
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ProFit AI", page_icon="🔥", layout="centered")

# עיצוב CSS מתקדם לנייד
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    div.stButton > button:first-child {
        background-color: #00ffcc; color: black; font-weight: bold; border-radius: 20px; height: 3em;
    }
    .stProgress > div > div > div > div { background-color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 ProFit: Muscle & Abs")

# --- מערכת תזונה חכמה ---
with st.expander("🥗 תפריט 2000 קלוריות - מהיר"):
    cols = st.columns(2)
    cols[0].markdown("*חלבון:* חזה עוף, טונה, ביצים, יוגורט PRO")
    cols[1].markdown("*פחמימה:* אורז בסמטי, בטטה, שיבולת שועל")
    st.info("טיפ: הכן מראש (Meal Prep) ל-3 ימים כדי לחסוך זמן.")

# --- טיימר אימון אינטראקטיבי ---
st.header("🏋️ אימון מודרך (30 דק')")
mode = st.selectbox("בחר אימון:", ["ניפוח שריר (Hypertrophy)", "חיטוב וקוביות (Core)"])

exercises = {
    "ניפוח שריר (Hypertrophy)": ["סקוואט", "שכיבות סמיכה", "מתח/חתירה", "לחיצת כתפיים"],
    "חיטוב וקוביות (Core)": ["Leg Raises", "Bicycle Crunches", "Plank", "Mountain Climbers"]
}

current_workout = exercises[mode]

# טיימר
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

col1, col2 = st.columns(2)
duration = col1.number_input("שניות לתרגיל:", value=45)
sets = col2.number_input("מספר סטים:", value=4)

if st.button("🚀 התחל סבב אימון"):
    for s in range(int(sets)):
        for ex in current_workout:
            st.subheader(f"בצע: {ex}")
            bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(duration):
                time.sleep(1)
                bar.progress((i + 1) / duration)
                status_text.text(f"זמן נותר: {duration - i - 1} שניות")
            
            st.write(f"✅ סיימת {ex}!")
            st.audio("https://www.soundjay.com") # צליל סיום
            time.sleep(2) # מנוחה קצרה בין תרגילים
    st.balloons()

# --- מעקב התקדמות ויזואלי ---
st.divider()
st.header("📈 מעקב ניפוח שריר")
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["תאריך", "משקל"])

with st.form("progress_form"):
  w = st.number_input('משקל שהרמת היום (ק"ג):', step=0.5)
    submit = st.form_submit_button("שמור התקדמות")
    if submit:
        new_data = pd.DataFrame({"תאריך": [pd.Timestamp.now()], "משקל": [w]})
        st.session_state.data = pd.concat([st.session_state.data, new_data])

if not st.session_state.data.empty:
    fig = px.line(st.session_state.data, x="תאריך", y="משקל", title="גרף התקדמות כוח")
    fig.update_traces(line_color='#00ffcc')

    st.plotly_chart(fig, use_container_width=True)
