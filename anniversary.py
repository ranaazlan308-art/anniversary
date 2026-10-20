
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Forever & Always ❤️",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PERSONAL DETAILS
st.sidebar.title("💌 Personalize Your Surprise")
wife_name = st.sidebar.text_input("Wife ka naam", "Meri Jaan")
your_name = st.sidebar.text_input("Tumhara naam", "Tumhara Humsafar")
nikah_date = st.sidebar.date_input(
    "Nikah ki date",
    value=date(2022, 10, 29)
)

# ROMANTIC DESIGN
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600;700&display=swap');

.stApp {
    background: linear-gradient(145deg, #160b16, #351127, #170d20);
    color: #fff0f5;
    font-family: 'Poppins', sans-serif;
}
header[data-testid="stHeader"] {background: transparent;}
#MainMenu, footer {visibility: hidden;}

.hero {
    text-align: center;
    padding: 45px 10px 25px;
}
.hero h1 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(50px, 8vw, 88px);
    color: #ffb6d0;
    margin: 0;
    text-shadow: 0 0 25px #ff4081;
}
.hero p {
    font-size: 14px;
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
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 8px 35px rgba(255,64,129,0.08);
}
.script {
    font-family: 'Great Vibes', cursive;
    color: #ffb6d0;
    font-size: 40px;
}
.small {
    color: #f8d8e5;
    line-height: 1.9;
    font-size: 15px;
}
div.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 30px;
    border: 1px solid #ffb6d0;
    background: linear-gradient(90deg, #e83e78, #9d286e);
    color: white;
    font-weight: 600;
    transition: 0.3s;
}
div.stButton > button:hover {
    border-color: white;
    box-shadow: 0 0 20px #ff4081;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# HERO
st.markdown(f"""
<div class="hero">
    <div class="heart">💗</div>
    <h1>Forever & Always</h1>
    <p>A LOVE STORY BLESSED BY ALLAH</p>
    <h2 style="color:#ffe0eb;">For {wife_name} 💍</h2>
    <p>29 OCTOBER · OUR SPECIAL DAY</p>
</div>
""", unsafe_allow_html=True)


# ANNIVERSARY COUNTER
today = date.today()
years = today.year - nikah_date.year

if (today.month, today.day) < (nikah_date.month, nikah_date.day):
    years -= 1

days_together = max(0, (today - nikah_date).days)
years = max(0, years)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ffb6d0;">{years}</h1>
        <p>Beautiful Years 💕</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ffb6d0;">{days_together}</h1>
        <p>Days Together 🌙</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h1 style="color:#ffb6d0;">∞</h1>
        <p>Love For You ❤️</p>
    </div>
    """, unsafe_allow_html=True)


# LOVE LETTER
st.markdown(f"""
<div class="card">
    <div class="script">My Dearest Love, 💌</div>
    <div class="small">
    Meri jaan, jab se tum meri zindagi ka hissa bani ho,
    meri duniya pehle se zyada khoobsurat ho gayi hai.<br><br>

    Hamare Nikah ke din se lekar aaj tak, tum mere liye
    sirf meri humsafar nahi, balkay meri khushi aur mera sukoon ho.<br><br>

    Ho sakta hai main har roz apne dil ki har baat alfaaz mein
    na keh sakun, lekin tum mere liye bohat special ho.<br><br>

    Meri dua hai ke hum hamesha ek doosre ko samjhein,
    ek doosre ki izzat karein aur har mushkil mein saath kharay rahein.<br><br>

    <b>Happy Anniversary, meri jaan! ❤️</b><br>
    Allah hamare rishte mein hamesha mohabbat, rehmat aur barkat rakhe.
    Ameen.
    </div>
    <br>
    <div class="script" style="text-align:right;">
        Forever yours 💖
    </div>
</div>
""", unsafe_allow_html=True)


# SURPRISE 1
st.markdown("""
<div class="hero">
    <h1 style="font-size:60px;">Surprise Number One 🎁</h1>
    <p>A LITTLE MESSAGE FROM MY HEART</p>
</div>
""", unsafe_allow_html=True)

if st.button("💝 Open Your First Surprise"):
    st.balloons()
    st.session_state["surprise1"] = True

if st.session_state.get("surprise1", False):
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div style="font-size:55px;">❤️🌹❤️</div>
        <div class="script">You Are My Favourite Person</div>
        <p class="small">
        {wife_name}, duniya mein bohat si khoobsurat cheezein hain,
        lekin mere liye tumhari muskurahat se zyada khoobsurat kuch nahi.<br><br>
        Tumhari khushi meri khushi hai aur tumhara saath meri zindagi
        ka sab se pyara tohfa hai.<br><br>
        I love you more than words can ever explain. 💗
        </p>
    </div>
    """, unsafe_allow_html=True)


# SURPRISE 2
st.markdown("""
<div class="hero">
    <h1 style="font-size:60px;">Surprise Number Two 💌</h1>
    <p>OPEN THIS WHEN YOU MISS ME</p>
</div>
""", unsafe_allow_html=True)

if st.button("💌 Open My Secret Letter"):
    st.session_state["surprise2"] = True
    st.snow()

if st.session_state.get("surprise2", False):
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div style="font-size:55px;">💌🫶🏻💗</div>
        <div class="script">Whenever You Miss Me...</div>
        <p class="small">
        Meri jaan {wife_name}, agar kabhi tumhein meri yaad aaye,
        toh apni aankhein band karke hamare khoobsurat lamhon ko yaad karna.<br><br>
        Yaad rakhna, faaslay chahe jitne bhi hon, tum mere dil mein
        hamesha ek khaas jagah rakhti ho.<br><br>
        Kaash main is waqt tumhare paas hota, tumhara haath pakarta
        aur tumhein batata ke tum mere liye kitni important ho.<br><br>
        <b>Jab bhi mujhe yaad karo, samajhna mera dil bhi tumhein
        yaad kar raha hai. ❤️</b>
        </p>
        <div class="script">Your person, always 💕</div>
    </div>
    """, unsafe_allow_html=True)


# SURPRISE 3
st.markdown("""
<div class="hero">
    <h1 style="font-size:60px;">Surprise Number Three 💍</h1>
    <p>OUR FOREVER PROMISE</p>
</div>
""", unsafe_allow_html=True)

if st.button("💍 Discover Our Forever Promise"):
    st.session_state["surprise3"] = True
    st.balloons()

if st.session_state.get("surprise3", False):
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div style="font-size:60px;">💍❤️♾️</div>
        <div class="script">My Promise To You</div>
        <p class="small">
        Aaj hamare Nikah ko chaar saal ho gaye hain,
        aur meri dua hai ke hamari kahani ka safar
        zindagi bhar chalta rahe.<br><br>
        Main wada karta hoon ke tumhari baat sunne ki,
        tumhari izzat karne ki aur hamare rishte ko mazboot
        banane ki hamesha koshish karunga.<br><br>
        Main chahta hoon ke hum sirf aaj nahi,
        balkay apni zindagi ke har aane wale din ko
        ek khoobsurat yaad banayein.<br><br>
        Allah humein hamesha ek doosre ke liye khair,
        sukoon aur khushi ka zariya banaye. Ameen. 🤲🏻<br><br>
        <b>My favourite chapter is the one I get to spend with you.</b>
        </p>
        <div class="script">You, Me & Forever 💖</div>
        <h3 style="color:#ffe0eb;">With all my love, {your_name}</h3>
    </div>
    """, unsafe_allow_html=True)


# FINAL FOOTER
st.markdown("""
<hr style="border-color:#61304e;">
<div style="text-align:center;padding:20px;">
    <div class="script">One Nikah. Two Hearts. One Lifetime. 💍</div>
    <p style="color:#e9b8cd;">
        Made with love, prayers and endless memories ❤️<br>
        Forever & Always.
    </p>
</div>
""", unsafe_allow_html=True)
