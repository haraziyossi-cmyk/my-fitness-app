import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="ProFit Coach AI", page_icon="🏋️")

# --- עיצוב ממשק ---
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

st.title("💪 מאמן אישי ותזונה")

# --- מחשבון חלבון ---
with st.expander("📊 מחשבון חלבון יומי"):
    weight_kg = st.number_input("הכנס משקל (קג):", min_value=1.0, value=75.0, step=0.5)
    protein_target = weight_kg * 2.0
    st.success(f"מטרת החלבון היומית שלך: *{protein_target:.0f} גרם* (כדי לבנות שריר).")

# --- תוכנית תזונה (ללא בוקר) ---
with st.expander("🥗 תוכנית תזונה (עד 2000 קל' - ללא בוקר)"):
    st.subheader("ארוחות עשירות בחלבון וקלות להכנה")
    st.markdown("""
    *   *ארוחת צהריים (כ-800 קלוריות):* 200 גרם חזה עוף/דג, כוס אורז/קינואה, ירקות.
    *   *ארוחת ביניים (כ-300 קלוריות):* יוגורט יווני (Pro) או קוטג' 5%, פרי.
    *   *ארוחת ערב (כ-700 קלוריות):* טונה במים/ביצים, 2 פרוסות לחם מלא, סלט ירקות.
    *   *סה"כ כ-1800 קלוריות.*
    """)

# --- בניית התוכנית המקצועית ---
workout_db = {
    "יום א' (Push): חזה, כתפיים ויד אחורית": [
        {"name": "שכיבות סמיכה רחבות", "reps": "4 סטים X 12 חזרות", "desc": "דגש על חזה", "video": "https://www.youtube.com"},
        {"name": "לחיצת כתפיים (משקולות)", "reps": "3 סטים X 10 חזרות", "desc": "כתפיים רחבות", "video": "https://www.youtube.com"},
        {"name": "פשיטת מרפקים מעל הראש", "reps": "3 סטים X 12 חזרות", "desc": "יד אחורית (Triceps)", "video": "https://www.youtube.com"},
        {"name": "קפיצה בחבל", "reps": "5 סבבים של דקה", "desc": "פעילות אירובית", "video": "https://www.youtube.com"}
    ],
    "יום ב' (Pull): גב ויד קדמית": [
        {"name": "חתירה עם משקולות", "reps": "4 סטים X 12 חזרות", "desc": "עיבוי הגב", "video": "https://www.youtube.com"},
        {"name": "כפיפת מרפקים (Biceps)", "reps": "3 סטים X 12 חזרות", "desc": "ניפוח היד הקדמית", "video": "https://www.youtube.com"},
        {"name": "פלאנק (Plank)", "reps": "3 סטים X 60 שניות", "desc": "חיזוק הליבה", "video": "https://www.youtube.com"},
        {"name": "קפיצה בחבל", "reps": "5 סבבים של דקה", "desc": "פעילות אירובית", "video": "https://www.youtube.com"}
    ],
    "יום ג' (Legs & Abs): רגליים ובטן": [
        {"name": "סקוואט עם משקולות", "reps": "4 סטים X 15 חזרות", "desc": "בניית רגליים", "video": "https://www.youtube.com"},
        {"name": "מכרעים (Lunges)", "reps": "3 סטים X 12 לכל רגל", "desc": "עיצוב הישבן והירך", "video": "https://www.youtube.com"},
        {"name": "הרמת רגליים בשכיבה", "reps": "4 סטים X 15 חזרות", "desc": "קוביות בבטן", "video": "https://www.youtube.com"},
        {"name": "קפיצה בחבל", "reps": "8 סבבים של דקה", "desc": "פעילות אירובית", "video": "https://www.youtube.com"}
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
            <code>{ex['reps']}</code><br>
            <a href="{ex['video']}" target="_blank">📺 צפה בהסבר וידאו קצר</a>
        </div>""", unsafe_allow_html=True)

# --- טיימר אימון חכם ---
st.divider()
st.subheader("Workout Timer")
