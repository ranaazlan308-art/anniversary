import streamlit as st
from datetime import date
import base64

st.set_page_config(
    page_title="Forever & Always ❤️",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- PERSONAL DETAILS ----------
st.sidebar.title("💌 Personalize Your Surprise")
wife_name = st.sidebar.text_input("Wife ka naam", "Meri Jaan")
your_name = st.sidebar.text_input("Tumhara naam", "Tumhara Humsafar")
nikah_date = st.sidebar.date_input(
    "Nikah ki date",
    value=date(2022, 10, 29)
)

# ---------- ROMANTIC DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600;700&display=swap');

.stApp {
    background: linear-gradient(145deg, #160b16, #351127, #170d20);
    color: #fff0f5;
    font-family: 'Poppins', sans-serif;
}
header[data-testid="stHeader"] {
    background: transparent;
}
#MainMenu, footer {visibility: hidden;}

.hero {
    text-align: center;
    padding: 65px 12px 35px 12px;
}
.hero h1 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(55px, 9vw, 100px);
    color: #ffb6d0;
    margin: 0;
    text-shadow: 0 0 25px #ff4081;
}
.hero p {
    font-size: 17px;
    letter-spacing: 2px;
    color: #f8d8e5;
}
.heart {
    font-size: 48px;
    animation: beat 1.2s infinite;
    display: inline-block;
}
@keyframes beat {
    0%, 100% {transform: scale(1);}
    50% {transform: scale(1.2);}
}
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,182,208,0.35);
    border-radius: 22px;
    padding: 28px;
    margin: 18px 0;
    box-shadow: 0 8px 35px rgba(255,64,129,0.08);
}
.script {
    font-family: 'Great Vibes', cursive;
    color: #ffb6d0;
    font-size: 42px;
}
.small {
    color: #f8d8e5;
    line-height: 1.9;
    font-size: 16px;
}
div.stButton > button {
    width: 100%;
    border-radius: 30px;
    border: 1px solid #ffb6d0;
    background: linear-gradient(90deg, #e83e78, #9d286e);
    color: white;
    padding: 13px 20px;
    font-weight: 600;
    transition: 0.3s;
}
div.stButton > button:hover {
    border-color: white;
    box-shadow: 0 0 20px #ff4081;
    color: white;
}
div[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.04);
    padding: 15px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="hero">
    <div class="heart">💗</div>
    <h1>Forever & Always</h1>
    <p>A LOVE STORY WRITTEN BY ALLAH'S BLESSINGS</p>
    <h2 style="color:#ffe0eb;">For {wife_name} 💍</h2>
    <p>29 OCTOBER · OUR SPECIAL DAY</p>
</div>
""", unsafe_allow_html=True)

# ---------- ANNIVERSARY COUNTER ----------
today = date.today()
years = today.year - nikah_date.year
if (today.month, today.day) < (nikah_date.month, nikah_date.day):
    years -= 1

years = max(0, years)
days_together = max(0, (today - nikah_date).days)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ffb6d0;">{years}</h1>
        <p>Beautiful Years 💕</p>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ffb6d0;">{days_together}</h1>
        <p>Days Together 🌙</p>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ffb6d0;">∞</h1>
        <p>Love For You ❤️</p>
    </div>""", unsafe_allow_html=True)

# ---------- LOVE LETTER ----------
st.markdown("""
<div class="card">
    <div class="script">My Dearest Love, 💌</div>
    <div class="small">
    Meri jaan, jab se tum meri zindagi ka hissa bani ho,
    zindagi pehle se zyada khoobsurat lagti hai.<br><br>
    tum mere liye
    sirf meri humsafar nahi, balkay meri khushi, mera sukoon
    aur meri zindagi ka ek bohat pyara hissa ho.<br><br>
    Ho sakta hai main har roz apne dil ki har baat alfaaz mein
    na keh sakun, lekin tum mere liye bohat special ho.
    Main chahta hoon ke har aane wale saal mein hum saath
    hansein, ek doosre ko samjhein aur har mushkil mein
    ek doosre ka haath thaamein.<br><br>
    <b>Happy 4th Nikah Anniversary, meri jaan.</b><br>
    Meri dua hai ke hamara rishta hamesha mohabbat,
    izzat, rehmat aur barkat se bhara rahe. Ameen. ❤️
    </div>
    <br>
    <div class="script" style="text-align:right;">Forever yours 💖</div>
</div>
""", unsafe_allow_html=True)
# ---------- PROMISES ----------
st.markdown("""
<div class="card">
    <div class="script">My Promises To You 🌹</div>
    <div class="small">
    ❤️ I promise to keep choosing you, every single day.<br>
    ❤️ I promise to listen, understand and respect you.<br>
    ❤️ I promise to stand beside you in happy and difficult times.<br>
    ❤️ I promise to keep making little memories with you.<br>
    ❤️ I pray that we grow old together, with love in our hearts.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- SECRET SURPRISE ----------
st.markdown("""
<div class="hero" style="padding:20px 0;">
    <h1 style="font-size:65px;">One Last Surprise...</h1>
    <p>MADE WITH ALL MY HEART, JUST FOR YOU 💌</p>
</div>
""", unsafe_allow_html=True)

if "surprise_open" not in st.session_state:
    st.session_state.surprise_open = False

if st.button("🎁 Open Your Special Surprise ❤️"):
    st.session_state.surprise_open = True
    st.balloons()

if st.session_state.surprise_open:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div style="font-size:65px;">💍❤️🧿</div>
        <div class="script">You Are My Forever</div>
        <h2 style="color:#ffe0eb;">{wife_name}, meri jaan...</h2>
        <p class="small">
        Mariyam Agar mujhe zindagi dobara shuru karne ka mauqa mile,
        toh main phir tumhein hi chunoon.<br><br>
        Tumhare saath guzra har lamha mere liye ek tohfa hai.
        Main perfect nahi hoon, lekin tumse meri mohabbat
        dil se hai.<br><br>
        <b>4 saal guzr gaye, aur meri dua hai ke hamari
        mohabbat har guzarte saal ke saath aur mazeed gehri ho. ❤️</b>
        </p>
        <div class="script">I Love You sooo muchhhh meri jaaaan mera bachaaaaa, Always & Forever 💗</div>
        <p style="color:#ffb6d0;">With love, {your_name}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr style="border-color:#61304e;">
<p style="text-align:center;color:#e9b8cd;padding:15px;">
Made with ❤️, prayers and endless love.<br>
One Nikah. Two hearts. A lifetime together. 💍
</p>
""", unsafe_allow_html=True)
