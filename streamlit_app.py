import streamlit as st
import google.generativeai as genai

# --- PROFESSIONAL UI: HIGH CONTRAST EDITION ---
st.set_page_config(page_title="Predict.pk", page_icon="🏏", layout="centered")

st.markdown("""
    <style>
    /* Professional Dark Theme with High Contrast */
    .stApp { background-color: #050a08; }
    
    /* Input Labels */
    label { color: #C5A059 !important; font-weight: bold !important; text-transform: uppercase; }

    /* Input Fields: Pure White for Readability */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: bold !important;
    }

    /* The Oracle's Response Box - FIXED CONTRAST */
    .stChatMessage { 
        background-color: #162C22 !important; 
        border: 2px solid #C5A059 !important;
        border-radius: 10px !important;
        padding: 20px !important;
    }
    
    /* FORCE WHITE TEXT FOR ORACLE */
    .stChatMessage p, .stChatMessage div { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
    }

    /* Professional Button */
    .stButton>button {
        background: linear-gradient(90deg, #C5A059 0%, #E6C681 100%);
        color: #050a08 !important;
        font-weight: 800 !important;
        border-radius: 8px;
        height: 55px;
        width: 100%;
        border: none;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE CONFIG ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-3-flash-preview')
except:
    st.error("API Key Missing.")

# --- APP UI ---
st.title("🏆 PREDICT.PK")
st.subheader("PSL 2026: THE ORACLE IS LIVE")

with st.container():
    st.markdown("---")
    st.write("📍 **MATCH 01:** Lahore Qalandars vs Hyderabad Kingsmen")
    
    winner = st.selectbox("WHICH TEAM IS TAKING THE W?", ["Select Team", "Lahore Qalandars", "Hyderabad Kingsmen"])
    stake = st.text_input("YOUR FUN STAKE", placeholder="e.g. Dinner on me!")

# --- ACTION ---
if st.button("REVEAL MY DESTINY"):
    if winner == "Select Team":
        st.warning("Select a team first, boss!")
    else:
        with st.spinner('Consulting the legends...'):
            try:
                prompt = f"User picks {winner}. Stake: {stake}. Give a witty, professional, high-energy PSL prediction. Use 'Lush' or 'Slogging' naturally. End with a 1-line WhatsApp Flex."
                response = model.generate_content(prompt)
                
                # Success Display
                st.balloons()
                with st.chat_message("assistant"):
                    st.markdown(response.text)
            except Exception as e:
                st.error("The stadium is too loud! Try clicking again.")

st.divider()
st.caption("© 2026 Predict.pk | Professional Beta v3.0")
