import streamlit as st
import google.generativeai as genai

# --- PROFESSIONAL UI STYLING ---
st.set_page_config(page_title="Predict.pk", page_icon="🏏", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #f1c40f; color: black; font-weight: bold; border: none; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #333; }
    .stSelectbox>div>div>div { background-color: #1a1a1a; color: white; }
    h1, h2, h3 { color: #f1c40f; text-transform: uppercase; letter-spacing: 2px; }
    .stAlert { background-color: #1a1a1a; color: #ffffff; border: 1px solid #f1c40f; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE SETUP ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Using the 2026 Production Model
    model = genai.GenerativeModel('gemini-3-flash')
except Exception as e:
    st.error("Engine Offline. Please check API Configuration.")

# --- APP HEADER ---
st.title("PREDICT.PK")
st.markdown("##### PAKISTAN'S #1 PREDICTION ENGINE")
st.info("🏏 **PSL 2026 OPENER:** Lahore Qalandars vs Hyderabad Kingsmen")

# --- USER INPUT ---
with st.container():
    winner = st.selectbox("CHOOSE YOUR WINNER", ["Select Team", "Lahore Qalandars", "Hyderabad Kingsmen"])
    stake = st.text_input("YOUR 'FUN STAKE'", placeholder="e.g., Dinner is on me if I lose!")

st.divider()

# --- PREDICTION LOGIC ---
if st.button("GET ORACLE'S BLESSING"):
    if winner == "Select Team":
        st.warning("PLEASE SELECT A TEAM TO CONTINUE.")
    else:
        with st.spinner('CONSULTING THE ORACLE...'):
            prompt = f"""
            System: Act as the professional but witty Oracle of predict.pk. 
            Context: PSL 2026 Match (LQ vs HK).
            User Selection: {winner}.
            User Stake: {stake}.
            Task: Provide a sharp, expert, family-friendly response. 
            Slang: Use 'Lush', 'Slogging', or 'Kaanpein Tang Rahi' naturally. 
            Output: Expert analysis + 1-line WhatsApp Flex.
            """
            try:
                response = model.generate_content(prompt)
                st.chat_message("assistant").write(response.text)
                st.balloons()
            except Exception as e:
                st.error("The Oracle is temporarily unreachable. Try again in 30 seconds.")

st.caption("© 2026 Predict.pk | Built with Google AI Studio")
