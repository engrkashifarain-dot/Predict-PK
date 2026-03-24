import streamlit as st
import google.generativeai as genai

# 1. Setup the Brain
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("🔑 Connection Error: Check your Streamlit Secrets for the API Key!")

# 2. Page Setup
st.set_page_config(page_title="Predict.pk", page_icon="🏏")
st.title("🏏 Predict.pk: PSL 2026")
st.markdown("### The Oracle is in the building. Slogging starts now!")

# 3. The Match Card
st.info("📅 **Opening Match:** Lahore Qalandars vs Hyderabad Kingsmen")
st.write("📍 *Gaddafi Stadium, Lahore | March 26, 8:00 PM PKT*")

st.divider()

# 4. Input Form
winner = st.selectbox("Who takes the win?", ["Select a team", "Lahore Qalandars", "Hyderabad Kingsmen"])
stake = st.text_input("Your 'Fun Stake'?", placeholder="e.g. I'll treat everyone to Chai!")

# 5. The Logic
if st.button("Get Oracle's Blessing"):
    if winner == "Select a team":
        st.warning("O bhai! Team select karain!")
    else:
        with st.spinner('Calculating the vibes...'):
            prompt = f"User predicts {winner} wins. Stake: {stake}. Give a witty, family-friendly Pakistani response. Use 'Lush' or 'Kaanpein Tang Rahi' if they fit. End with a 1-line WhatsApp Flex."
            try:
                response = model.generate_content(prompt)
                st.chat_message("assistant").write(response.text)
                st.balloons()
            except:
                st.write("The Oracle is stuck in Lahore traffic. Try again!")

st.divider()
st.caption("predict.pk | March 26th Launch | Built with Google AI Studio")
