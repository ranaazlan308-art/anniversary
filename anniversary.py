
# ==================================================
# ROMANTIC QUIZ — KOI BHI JAWAB ACCEPT HOGA
# ==================================================

if not st.session_state.quiz_unlocked:

    st.markdown("""
    <div class="hero">
        <div class="heart">💗</div>
        <h1>Forever &amp; Always</h1>
        <p>A LOVE STORY WRITTEN BY ALLAH'S BLESSINGS</p>
        <h2 style="color:#ffe0eb;">Sirf Meri Jaan Ke Liye 💍</h2>
    </div>

    <div class="card">
        <div class="script">Hamari Pyari Yaadein 💌</div>
        <p class="small">
        Meri jaan, in sawalon ke jawab apne dil se dena.
        Yahan koi sahi ya ghalat jawab nahi hai.
        Tumhare har jawab ki apni ahmiyat hai. ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("love_quiz"):
        answer1 = st.text_input(
            "💗 1. Hamari pehli mulaqat kahan hui thi?"
        )
        answer2 = st.text_input(
            "💗 2. Meri favourite cheez kya hai?"
        )
        answer3 = st.text_input(
            "💗 3. Hamari sab se pyari yaad kya hai?"
        )
        answer4 = st.text_input(
            "💗 4. Main tumhein pyar se kis naam se bulata hoon?"
        )

        submitted = st.form_submit_button(
            "❤️ Unlock My Surprise"
        )

    if submitted:
        answers = [answer1, answer2, answer3, answer4]

        if all(answer.strip() for answer in answers):
            st.session_state.quiz_unlocked = True
            st.balloons()
            st.rerun()
        else:
            st.warning(
                "Meri jaan, chaaron sawalon ke jawab likho. 💕"
            )

    st.markdown("""
    <p style="text-align:center;color:#e9b8cd;">
        Made with ❤️, prayers and endless love.
    </p>
    """, unsafe_allow_html=True)

    st.stop()
