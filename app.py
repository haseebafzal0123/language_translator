import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="GlobalTranslate Pro", 
    layout="wide", 
    page_icon="🌐"
)

# --- 2. Custom CSS for Styling ---
st.markdown("""
    <style>
    /* Overall page background */
    .main { background-color: #f8f9fa; }
    
    /* Input Text Area Styling */
    .stTextArea textarea { 
        border-radius: 12px !important; 
        border: 2px solid #0078D4 !important;
        font-size: 16px !important;
        background-color: #ffffff;
    }

    /* THE FIX: Translation Output Card Styling */
    /* Forced black text color (#1a1a1a) to ensure visibility on white background */
    .translation-card { 
        background-color: #ffffff; 
        color: #1a1a1a !important; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 6px solid #0078D4;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08); 
        min-height: 250px;
        margin-bottom: 15px;
        font-size: 18px;
        line-height: 1.6;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Center the title */
    .title-text {
        text-align: center;
        color: #0078D4;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header Section ---
st.markdown("<h1 class='title-text'>🌐 GlobalTranslate Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>High-Performance AI Text Translation</p>", unsafe_allow_html=True)
st.divider()

# --- 4. Main UI Layout (Two Columns) ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 Input Text")
    # Language Selection for Source
    src_lang_name = st.selectbox(
        "Source Language:", 
        ["auto-detect"] + list(LANGUAGES.values()), 
        key="src"
    )
    
    # Input Area
    input_text = st.text_area(
        "Type or paste your text here:", 
        height=300, 
        placeholder="e.g. The Brinell hardness test is used for metallic materials..."
    )

with col2:
    st.markdown("### 📤 Translation")
    # Language Selection for Target (Defaulting to Urdu)
    trg_lang_name = st.selectbox(
        "Target Language:", 
        list(LANGUAGES.values()), 
        index=list(LANGUAGES.values()).index('urdu'), 
        key="trg"
    )
    
    # Logic Processing
    if input_text.strip():
        try:
            # Map full language name to ISO code
            dest_code = [k for k, v in LANGUAGES.items() if v == trg_lang_name][0]
            src_code = 'auto' if src_lang_name == "auto-detect" else [k for k, v in LANGUAGES.items() if v == src_lang_name][0]
            
            # Show a spinner while the API works
            with st.spinner("AI is translating..."):
                result = translator.translate(input_text, src=src_code, dest=dest_code)
            
            # Display Translation in the styled card
            st.markdown(f'<div class="translation-card">{result.text}</div>', unsafe_allow_html=True)
            
            # Add a copy-able code block for the user's convenience
            st.caption("Click the icon on the right to copy:")
            st.code(result.text, language=None)
                    
        except Exception:
            st.error("There was a temporary connection issue. Please try clicking translate again.")
    else:
        # Placeholder when no text is entered
        st.info("The translated text will appear here once you provide input.")

# --- 5. Footer Section ---
st.divider()
st.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 0.9em;'>"
    "Developed by <b>Abdul Haseeb</b> | AI Internship Task 2026"
    "</p>", 
    unsafe_allow_html=True
)