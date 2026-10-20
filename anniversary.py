
import streamlit as st
from datetime import date
import html

st.set_page_config(
    page_title="Forever & Always ❤️",
    page_icon="💍",
    layout="wide"
)

# Initialize session state before using it
if "quiz_unlocked" not in st.session_state:
    st.session_state["quiz_unlocked"] = False

if "surprise_open" not in st.session_state:
    st.session_state["surprise_open"] = False

# Romantic styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #1b0b1b, #45152f, #160b20);
    color: #fff0f5;
    font-family: 'Poppins', sans-serif;
}
#MainMenu, footer {visibility: hidden;}

.hero {
    text-align: center;
    padding: 35px 10px;
}
.hero h1 {
    font-family: 'Great Vibes', cursive;
    font-size: 75px;
    color: #ffb6d0;
    text-shadow: 0 0 20px #ff4081;
}
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid #a94b76;
    border-radius: 20px;
    padding: 25px;
    margin: 15px 0;
}
.script {
    font-family: 'Great Vibes', cursive;
    font-size: 42px;
    color: #ffb6d0;
}
.small {
    color: #ffe0eb;
    line-height: 1.9;
}
div.stButton > button,
div.stFormSubmitButton > button {
    width: 100%;
    border-radius: 25px;
    background: #d63375;
    color: white;
    border: 1px solid #ffb6d0;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# Four-question quiz
questions = [
    "Hamari pehli mulaqat kahan hui thi?",
    "Meri favourite cheez kya hai?",
    "Hamari sab se pyari yaad kya hai?",
    "Main tumhein pyar se kis naam se bulata hoon?"
]

# Show quiz until all answers are provided
if not st.session_state["quiz_unlocked"]:

    st.markdown("""
    <div class="hero">
        <h1>Forever & Always ❤️</h1>
        <h2>Sirf Meri Jaan Ke Liye 💍</h2>
        <p>Hamari pyari yaadon ka chhota sa quiz 💌</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("love_quiz"):
        answers = []

        for i, question in enumerate(questions, start=1):
            answer = st.text_input(
                f"Sawal {i}: {question}",
                key=f"answer_{i}",
                placeholder="Apna jawab likhein..."
            )
            answers.append(answer)

        submitted = st.form_submit_button(
            "❤️ Unlock My Surprise"
        )

    if submitted:
        if all(answer.strip() for answer in answers):
            st.session_state["quiz_unlocked"] = True
            st.rerun()
        else:
            st.warning(
                "Meri jaan, pehle chaaron sawalon ke jawab likho ❤️"
            )

    st.stop()

# Personal details
st.sidebar.title("💌 Personalize Your Website")

wife_name = st.sidebar.text_input(
    "Wife ka naam", "Meri Jaan"
)
your_name = st.sidebar.text_input(
    "Aapka naam", "Tumhara Humsafar"
)
nikah_date = st.sidebar.date_input(
    "Nikah ki date",
    value=date(2022, 10, 29),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# Safe display of names
wife = html.escape(wife_name)
your = html.escape(your_name)

today = date.today()
days_together = max(0, (today - nikah_date).days)

years = today.year - nikah_date.year
if (today.month, today.day) < (
    nikah_date.month, nikah_date.day
):
    years -= 1
years = max(0, years)

# Main heading
st.markdown(f"""
<div class="hero">
    <h1>Forever & Always ❤️</h1>
    <h2>For {wife} 💍</h2>
    <p>Our love story began on {nikah_date.strftime("%d %B %Y")}</p>
</div>
""", unsafe_allow_html=True)

# Anniversary counter
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card" style="text-align:center">
        <h1 style="color:#ffb6d0">{years}</h1>
        <p>Beautiful Years 💕</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card" style="text-align:center">
        <h1 style="color:#ffb6d0">{days_together}</h1>
        <p>Days Together 🌙</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align:center">
        <h1 style="color:#ffb6d0">∞</h1>
        <p>Love Forever ❤️</p>
    </div>
    """, unsafe_allow_html=True)

# Love letter

st.markdown(f"""
<div class="card">
    <div class="script">My Dearest Love 💌</div>
    <div class="small">
        Meri jaan {wife}, tum meri zindagi ka bohat khoobsurat
        hissa ho. Tumhare saath guzra har lamha mere liye
        ek anmol tohfa hai. ❤️
        <br><br>
        Main dua karta hoon ke hamara rishta hamesha mohabbat,
        izzat, sukoon aur barkat se bhara rahe. Har khushi aur
        mushkil mein hum ek doosre ka saath dein.
        <br><br>
        Main perfect nahi hoon, lekin tumse meri mohabbat
        dil se hai. Allah humein hamesha saath aur khush rakhe.
        Ameen. ❤️
    </div>
    <div class="script" style="text-align:right">
        Forever Yours 💖
    </div>
</div>
""", unsafe_allow_html=True)

# Promises
st.markdown("""
<div class="card">
    <div class="script">My Promises To You 🌹</div>
    <div class="small">
        ❤️ Main har din tumhein choose karunga.<br>
        ❤️ Main tumhari izzat aur feelings ka khayal rakhunga.<br>
        ❤️ Main har mushkil mein tumhara saath dunga.<br>
        ❤️ Main tumhare saath nayi yaadein banaunga.<br>
        ❤️ Main dua karta hoon ke hum saath boodhe hon.
    </div>
</div>
""", unsafe_allow_html=True)

# Secret surprise
st.markdown("""
<div class="hero">
    <h1>One Last Surprise 🎁</h1>
</div>
""", unsafe_allow_html=True)

if st.button("Open Your Special Surprise ❤️"):
    st.session_state["surprise_open"] = True
    st.balloons()

if st.session_state["surprise_open"]:
    st.markdown(f"""
    <div class="card" style="text-align:center">
        <div class="script">You Are My Forever 💍</div>
        <h2>{wife}, Meri Jaan ❤️</h2>
        <div class="small">
            Agar mujhe dobara zindagi shuru karne ka mauqa mile,
            toh main phir tumhein hi chunoon.<br><br>
            Tum meri khushi, mera sukoon aur meri favourite
            insan ho. Main tumse aaj bhi mohabbat karta hoon
            aur hamesha karta rahunga. ❤️
        </div>
        <div class="script">I Love You soooo mucchhhhhh meri jaaan mera bachaaaaaa 💗</div>
        <p>With love, {your}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr>
<p style="text-align:center;color:#ffb6d0">
Made with ❤️, prayers and endless love.
</p>
""", unsafe_allow_html=True)
