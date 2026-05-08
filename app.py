import streamlit as st
from googletrans import Translator, LANGUAGES

translator = Translator()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GlobalTranslate Pro",
    layout="wide",
    page_icon="🌐"
)

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.title-text {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: #00C6FF;
    margin-bottom: 0;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #d1d1d1;
    font-size: 18px;
    margin-top: 0;
}

/* Glass Box */
[data-testid="column"] {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

/* --- FIXED TEXTAREA CSS --- */
.stTextArea textarea {
    background-color: #1e2a3a !important; /* Solid dark background for contrast */
    color: #ffffff !important;           /* Pure white text */
    border-radius: 15px !important;
    border: 2px solid #00C6FF !important;
    font-size: 18px !important;
    padding: 15px !important;
}

/* Ensure the label above the textarea is also visible */
.stTextArea label p {
    color: #00C6FF !important;
    font-weight: bold;
}

/* --- END OF FIX --- */

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 12px;
    color: white;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 15px;
    height: 3.2em;
    border: none;
    background: linear-gradient(to right, #00C6FF, #0072FF);
    color: white;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 15px rgba(0,198,255,0.6);
}

/* Output Card FIXED */
.translation-card {
    background: rgba(255,255,255,0.18);
    padding: 25px;
    border-radius: 188px;
    border-left: 6px solid #00C6FF;
    color: #ffffff;
    font-size: 20px;
    line-height: 1.7;
    min-height: 120px;
    margin-top: 10px;
    overflow-wrap: break-word;
}

/* Footer */
.footer {
    text-align: center;
    color: #d1d1d1;
    font-size: 14px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='title-text'>🌐 GlobalTranslate Pro</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>High-Performance AI Text Translation</p>", unsafe_allow_html=True)

st.divider()

# ---------------- STATE ----------------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2, gap="large")

# ---------------- INPUT ----------------
with col1:
    st.markdown("## 📥 Input Text")

    src_lang_name = st.selectbox(
        "Source Language",
        ["auto-detect"] + list(LANGUAGES.values())
    )

    input_text = st.text_area(
        "Type or paste your text here:",
        height=320,
        placeholder="Enter text to translate..."
    )

# ---------------- OUTPUT ----------------
with col2:
    st.markdown("## 📤 Translation")

    trg_lang_name = st.selectbox(
        "Target Language",
        list(LANGUAGES.values()),
        index=list(LANGUAGES.values()).index("urdu")
    )

    # ---------------- TRANSLATE BUTTON ----------------
    translate_btn = st.button("🚀 Translate Now")

    if translate_btn:
        if input_text.strip():
            try:
                dest_code = [k for k, v in LANGUAGES.items() if v == trg_lang_name][0]
                src_code = (
                    "auto"
                    if src_lang_name == "auto-detect"
                    else [k for k, v in LANGUAGES.items() if v == src_lang_name][0]
                )

                with st.spinner("Translating..."):
                    result = translator.translate(
                        input_text,
                        src=src_code,
                        dest=dest_code
                    )
                st.session_state.translated_text = result.text

            except Exception:
                st.error("Translation failed. Please try again.")
        else:
            st.warning("Please enter text first.")

# ---------------- DISPLAY OUTPUT ----------------
if st.session_state.translated_text:
    st.markdown(
        f"""
        <div class="translation-card">
            {st.session_state.translated_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("📋 Copy translated text:")
    st.code(st.session_state.translated_text, language="text")

    if st.button("📋 Copy Text"):
        st.success("Text ready to copy from above box 👆")
else:
    st.info("Translated text will appear here after clicking Translate.")

# ---------------- FOOTER ----------------
st.divider()

st.markdown("""
<div class='footer'>
    Developed by <b>Abdul Haseeb</b> | AI Internship Task 2026
</div>
""", unsafe_allow_html=True)