import streamlit as st
import google.generativeai as genai

# --- PREMIUM UI THEMING ---
st.set_page_config(page_title="Predict.pk", page_icon="🏏", layout="centered")

# Custom CSS for Professionalism and Readability
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0B1C14; }
    
    /* Card Container */
    .prediction-card {
        background-color: #162C22;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #C5A059;
        margin-bottom: 20px;
    }
    
    /* Headers */
    h1 { color: #C5A059 !authoritative; font-family: 'Arial Black'; text-transform: uppercase; }
    h3 { color: #FFFFFF; font-weight: 300; }
    
    /* Input Fields - Fixing Readability */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 8px !important;
    }
    
    /* Professional Button */
    .stButton>button {
        background: linear-gradient(90deg, #C5A059 0%, #E6C681 100%);
        color: #0B1C14;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }
    
    /* Oracle Message Area */
    .stChatMessage { background-color: #1E3D30; border-left: 5px solid #C5A059; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE CONFIGURATION (GEMINI 3) ---
try:
    # Fetching the Secret Key you added in Streamlit
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # UPDATED: Using the 2026 Production-Grade Model
    model = genai.GenerativeModel('gemini-3-flash-preview')
except Exception as e:
    st.error("🔑 Engine Config Error: Please ensure GEMINI_API_KEY is in Streamlit Secrets.")

# --- APP LAYOUT ---
st.title("PREDICT.PK")
st.markdown("### 🏆 The Official PSL 2026 Oracle")

with st.container():
    st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
    
    st.write("📍 **MATCH 01:** Lahore Qalandars vs Hyderabad Kingsmen")
    
    col1, col2 = st.columns(2)
    with col1:
        winner = st.selectbox("PICK YOUR WINNER", ["Select Team", "Lahore Qalandars", "Hyderabad Kingsmen"])
    with col2:
        stake = st.text_input("YOUR 'FUN STAKE'", placeholder="e.g. Dinner on me!")

    st.markdown('</div>', unsafe_allow_html=True)

# --- EXECUTION ---
if st.button("REVEAL MY DESTINY"):
    if winner == "Select Team":
        st.warning("Pehle team to select karain! (Please select a team).")
    else:
        with st.spinner('Consulting the legends at Gaddafi Stadium...'):
            try:
                # The Prompt logic
                prompt = f"System: Witty PSL Expert. User picks {winner}. Stake: {stake}. Give a short, lush, professional prediction. Use 'Andhi Mar Rha' or 'Slogging' if they are too optimistic. End with a 1-line WhatsApp status Flex."
                
                response = model.generate_content(prompt)
                
                # Display Result
                st.chat_message("assistant").write(response.text)
                st.balloons()
            except Exception as e:
                # If it still fails, this will tell us EXACTLY why (Quota, Model, etc.)
                st.error(f"The Oracle is currently slogging through some errors. Details: {e}")

st.divider()
st.caption("© 2026 Predict.pk | Built with Google AI Studio | Official PSL Launch Version")
