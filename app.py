import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="ProFit Home Workout", page_icon="💪")

# --- עיצוב ממשק ---
# שינוי הרקע לבהיר וצבע הטקסט לכהה
st.markdown("""
    <style>
    /* רקע בהיר לכל האפליקציה וטקסט שחור */
    .stApp { background-color: #f0f2f6; color: black; }
    /* כפתורים */
    div.stButton > button:first-child { width: 100%; border-radius: 15px; height: 3.5em; background-color: #00ffcc; color: black; font-weight: bold; }
    /* רקע בהיר לתיבות התרגילים עם טקסט שחור */
    .exercise-box { padding: 15px; border-radius: 10px; background-color: #ffffff; margin-bottom: 10px; border-right: 5px solid #00ffcc; color: black; }
    /* כותרות ראשיות */
    h1, h2, h3, h4, h5, h6 { color: black; }
    /* הטקסט הכללי שאינו כותרת */
    .css-fg4pbf { color: black; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏋️ ProFit: תוכנית אימונים ביתית")
st.write("תוכנית אימונים יומית מפורטת")

# --- בניית התוכנית המקצועית ---
workout_db = {
    "יום א' (Push): חזה, כתפיים ויד אחורית": [
        {"name": "שכיבות סמיכה רחבות", "reps": "4 סטים X 12 חזרות", "desc": "דגש על חזה"},
        {"name": "לחיצת כתפיים (משקולות)", "reps": "3 סטים X 10 חזרות", "desc": "כתפיים רחבות"},
        {"name": "פשיטת מרפקים מעל הראש", "reps": "3 סטים X 12 חזרות", "desc": "יד אחורית (Triceps)"},
        {"name": "קפיצה בחבל", "reps": "5 סבבים של דקה", "desc": "פעילות אירובית"}
    ],
    "יום ב' (Pull): גב ויד קדמית": [
        {"name": "חתירה עם משקולות", "reps": "4 סטים X 12 חזרות", "desc": "עיבוי הגב"},
        {"name": "כפיפת מרפקים (Biceps)", "reps": "3 סטים X 12 חזרות", "desc": "ניפוח היד הקדמית"},
        {"name": "פלאנק (Plank)", "reps": "3 סטים X 60 שניות", "desc": "חיזוק הליבה"},
        {"name": "קפיצה בחבל", "reps": "5 סבבים של דקה", "desc": "פעילות אירובית"}
    ],
    "יום ג' (Legs & Abs): רגליים ובטן": [
        {"name": "סקוואט עם משקולות", "reps": "4 סטים X 15 חזרות", "desc": "בניית רגליים"},
        {"name": "מכרעים (Lunges)", "reps": "3 סטים X 12 לכל רגל", "desc": "עיצוב הישבן והירך"},
        {"name": "הרמת רגליים בשכיבה", "reps": "4 סטים X 15 חזרות", "desc": "קוביות בבטן"},
        {"name": "קפיצה בחבל", "reps": "8 סבבים של דקה", "desc": "פעילות אירובית"}
    ]
}

# --- בחירת אימון ---
day = st.selectbox("בחר אימון להיום:", list(workout_db.keys()))

st.subheader("📋 רשימת תרגילים")
for ex in workout_db[day]:
    with st.container():
        st.markdown(f"""<div class="exercise-box">
            <b>{ex['name']}</b><br>
            <small>{ex['desc']}</small><br>
            <code>{ex['reps']}</code>
        </div>""", unsafe_allow_html=True)

# --- טיימר אימון חכם ---
st.divider()
st.subheader("⏱️ טיימר עבודה ומנוחה")
t_duration = st.number_input("שניות לסט/מנוחה:", value=45)

if st.button("🚀 התחל סט!"):
    bar = st.progress(0)
    placeholder = st.empty()
    for i in range(int(t_duration)):
        time.sleep(1)
        remaining = int(t_duration) - i - 1
        bar.progress((i + 1) / int(t_duration))
        placeholder.metric("זמן נותר", f"{int(t_duration)-i-1} שניות")
    st.audio("https://www.soundjay.com")
    st.success("סיימת סט! רשום משקל ועבור לסט הבא.")
    st.balloons()

# --- מעקב משקלי עבודה ---
st.divider()
st.subheader("📈 יומן אימון")
ex_name = st.text_input("שם התרגיל שביצעת:")
weight_val = st.number_input("משקל שהרמת (קג):", step=0.5)

if st.button("💾 שמור התקדמות"):
    st.toast(f"מעולה! רשמנו {weight_val} קג ב-{ex_name}.")
