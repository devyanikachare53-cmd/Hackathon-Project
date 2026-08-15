
        4. Review the model output
        5. Read general health guidance
        """
    )

    st.divider()

    st.markdown("### 📌 Important")

    st.warning(
        "This application is an educational screening "
        "prototype. It is not a medical diagnosis."
    )

    st.divider()

    st.caption(
        "AI Health Assistant • Hackathon Prototype"
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🩺 AI Health Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Understand your symptoms with an AI-powered screening assistant.'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="info-box">
    <b>Welcome!</b><br>
    Enter your current symptoms below. The machine-learning model
    will analyze the entered values and provide its predicted class.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SYMPTOM INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🩺 Symptom Assessment</div>',
    unsafe_allow_html=True
)

left_col, right_col = st.columns([2.2, 1], gap="large")


# =========================================================
# LEFT SIDE - INPUTS
# =========================================================

with left_col:

    st.markdown(