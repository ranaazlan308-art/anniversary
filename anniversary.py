
import streamlit as st

st.set_page_config(
    page_title="Forever & Always ❤️",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- SESSION STATE ----------
for key in ["surprise1", "surprise2", "surprise3"]:
    if key not in st.session_state:
        st.session_state[key] = False

# ---------- PERSONALIZATION ----------
st.sidebar.title("💌 Personalize Your Website")
wife_name = st.sidebar.text_input("Her name / nickname", "My Love")
your_name = st.sidebar.text_input("Your name", "Your Forever Person")

# ---------- CSS DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #170b1c, #351126, #1a1028);
    color: #fff4f8;
    font-family: 'Poppins', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1050px;
    padding: 2rem 1.2rem 3rem;
}

.hero {
    text-align: center;
    padding: 35px 8px;
}

.hero h1 {
    font-family: 'Great Vibes', cursive;
    color: #ffb6d0;
    font-size: clamp(48px, 8vw, 82px);
    line-height: 1.3;
    text-shadow: 0 0 18px rgba(255, 64, 129, 0.45);
    overflow-wrap: anywhere;
}

.hero p {
    color: #ffe2ec;
    font-size: 14px;
    letter-spacing: 1.5px;
    line-height: 1.8;
}

.heart {
    font-size: 46px;
    animation: heartbeat 1.3s infinite;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.15); }
}

.love-card {
    background: #291527;
    border: 1px solid #a94b76;
    border-radius: 20px;
    padding: 25px;
    margin: 18px 0;
    overflow-wrap: anywhere;
}

.script-title {
    font-family: 'Great Vibes', cursive;
    color: #ffb6d0;
    font-size: clamp(32px, 5vw, 43px);
    line-height: 1.4;
    margin-bottom: 14px;
}

.love-text {
    color: #fff1f6;
    font-size: 16px;
    line-height: 2;
}

.counter {
    background: #291527;
    border: 1px solid #a94b76;
    border-radius: 18px;
    padding: 22px 8px;
    text-align: center;
    min-height: 135px;
}

.counter-number {
    color: #ffb6d0;
    font-size: 36px;
    font-weight: 700;
}

.counter-label {
    color: #fff1f6;
    font-size: 14px;
}

div.stButton > button {
    width: 100%;
    min-height: 55px;
    white-space: normal;
    background: #e83e78;
    color: #ffffff;
    border: 1px solid #ffb6d0;
    border-radius: 14px;
    font-weight: 700;
    font-size: 15px;
    padding: 12px;
}

div.stButton > button:hover {
    background: #bd2863;
    color: #ffffff;
    border-color: #ffffff;
}

div.stButton > button:focus {
    color: #ffffff;
    border-color: #ffffff;
}

div[data-testid="stSidebar"] {
    background: #241020;
}

div[data-testid="stSidebar"] * {
    color: #fff1f6;
}

hr {
    border-color: #a94b76 !important;
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 0.8rem 2rem;
    }

    .love-card {
        padding: 19px;
    }

    .love-text {
        font-size: 15px;
        line-height: 1.9;
    }

    .counter-number {
        font-size: 27px;
    }

    .counter-label {
        font-size: 12px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown(f"""
<div class="hero">
    <div class="heart">💗</div>
    <h1>Forever &amp; Always</h1>
    <p>A LITTLE WEBSITE MADE WITH A LOT OF LOVE</p>
    <h2 style="color:#ffffff;">For {wife_name} ❤️</h2>
    <p>YOU ARE MY FAVOURITE PERSON</p>
</div>
""", unsafe_allow_html=True)


# ---------- LOVE STATS ----------
st.markdown("""
<div class="hero" style="padding: 5px 0 15px;">
    <h1 style="font-size:48px;">Our Little World ✨</h1>
</div>
""", unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.markdown("""
    <div class="counter">
        <div class="counter-number">❤️</div>
        <div class="counter-label">A Heart Full of Love</div>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="counter">
        <div class="counter-number">∞</div>
        <div class="counter-label">Love Without Limits</div>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="counter">
        <div class="counter-number">1</div>
        <div class="counter-label">Favourite Person</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- LOVE LETTER ----------
st.markdown(f"""
<div class="love-card">
    <div class="script-title">My Dearest {wife_name}, 💌</div>
    <div class="love-text">
        Kabhi kabhi sochta hoon ke main tumhein bata bhi paata hoon
        ke tum mere liye kitni special ho ya nahi. ❤️<br><br>

        Tumhari muskurahat mere din ko khoobsurat bana deti hai.
        Tumse baat karna, tumhare saath hansna aur chhoti chhoti
        baatein share karna mere favourite moments hain.<br><br>

        Main perfect nahi hoon, lekin main hamesha koshish karna
        chahta hoon ke tum khush raho, tumhari izzat ho aur tumhein
        meri mohabbat ka ehsaas hota rahe.<br><br>

        Agar mujhe apni zindagi ke khoobsurat lamhon mein se
        ek cheez chunni ho, toh main tumhare saath guzare hue
        lamhon ko chununga. 💗<br><br>

        <b>You are not just a part of my life.
        You are one of my favourite reasons to smile.</b>
    </div>
    <br>
    <div class="script-title" style="text-align:right;">
        With all my love, 💕
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- SURPRISE ONE ----------
st.markdown("""
<div class="hero">
    <h1 style="font-size:54px;">A Little Surprise 🎁</h1>
    <p>SOMETHING SPECIAL JUST FOR YOU</p>
</div>
""", unsafe_allow_html=True)

if st.button("💝 Open Surprise Number One", key="btn1"):
    st.session_state.surprise1 = not st.session_state.surprise1
    if st.session_state.surprise1:
        st.balloons()

if st.session_state.surprise1:
    st.markdown(f"""
    <div class="love-card" style="text-align:center;">
        <div style="font-size:48px;">🌹❤️🌹</div>
        <div class="script-title">You Make My World Beautiful</div>
        <div class="love-text">
            {wife_name}, tumhari smile mere liye kisi magic se kam nahi.
            Tumhari khushi dekh kar mera dil khush ho jata hai.<br><br>

            Duniya chahe kitni bhi busy ho jaye, tumhare liye
            mere dil mein hamesha ek special jagah rahegi.<br><br>

            <b>Thank you for being you. I love you, meri jaan! ❤️</b>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------- SURPRISE TWO ----------
st.markdown("""
<div class="hero">
    <h1 style="font-size:54px;">A Secret Message 💌</h1>
    <p>OPEN THIS WHEN YOU MISS ME</p>
</div>
""", unsafe_allow_html=True)

if st.button("💌 Read Your Secret Letter", key="btn2"):
    st.session_state.surprise2 = not st.session_state.surprise2
    if st.session_state.surprise2:
        st.snow()

if st.session_state.surprise2:
    st.markdown(f"""
    <div class="love-card" style="text-align:center;">
        <div style="font-size:48px;">💌🫶🏻💗</div>
        <div class="script-title">Whenever You Miss Me...</div>
        <div class="love-text">
            Meri jaan {wife_name}, agar kabhi meri yaad aaye,
            toh hamari achhi baaton aur khoobsurat lamhon ko yaad karna.<br><br>

            Kaash main har us waqt tumhare paas hota jab tumhein
            ek hug, ek smile ya bas kisi apne ki zaroorat hoti.<br><br>

            Chahe hum paas hon ya door, tum mere liye bohat important ho.
            Main chahta hoon ke tum hamesha khud ko loved aur valued mehsoos karo.<br><br>

            <b>Jab tum mujhe miss karo, yaad rakhna:
            tum bhi mere dil ke bohat qareeb ho. ❤️</b>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------- SURPRISE THREE ----------
st.markdown("""
<div class="hero">
    <h1 style="font-size:54px;">One Last Surprise 💍</h1>
    <p>A PROMISE FROM MY HEART</p>
</div>
""", unsafe_allow_html=True)

if st.button("💍 Reveal My Promise", key="btn3"):
    st.session_state.surprise3 = not st.session_state.surprise3
    if st.session_state.surprise3:
        st.balloons()

if st.session_state.surprise3:
    st.markdown(f"""
    <div class="love-card" style="text-align:center;">
        <div style="font-size:55px;">💗♾️🌹</div>
        <div class="script-title">My Promise To You</div>
        <div class="love-text">
            {wife_name}, main promise karta hoon ke main tumhari baat
            sunne, tumhein samajhne aur tumhari izzat karne ki
            hamesha koshish karunga.<br><br>

            Main chahta hoon ke hum saath hansen, ek doosre se seekhein,
            mushkil waqt mein ek doosre ka sahara banen aur zindagi
            ki chhoti chhoti khushiyon ko celebrate karein.<br><br>

            Main tumse har roz perfect hone ka wada nahi karta,
            lekin apni mohabbat aur apne rawaiye ko behtar banane
            ki koshish ka wada zaroor karta hoon.<br><br>

            <b>My favourite place is wherever I can share a smile with you.</b>
        </div>
        <div class="script-title">You, Me &amp; Forever 💖</div>
        <h3 style="color:#ffffff;">With love, {your_name}</h3>
    </div>
    """, unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown("""
<hr>
<div class="hero">
    <h1 style="font-size:48px;">Always &amp; Forever 💗</h1>
    <p>MADE WITH LOVE, JUST FOR YOU</p>
    <p style="letter-spacing:0;">Two hearts, countless memories, endless possibilities. ❤️</p>
</div>
""", unsafe_allow_html=True)
