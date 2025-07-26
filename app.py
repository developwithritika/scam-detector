import streamlit as st
import joblib

# Load the trained model
model = joblib.load("scam_model.pkl")

# Streamlit App
st.title("Scam Message Detector (ML Powered)")

st.write("Paste any message below to check if it looks suspicious:")

user_input = st.text_area("Message:")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message to check.")
    else:
        # Predict probability
        proba = model.predict_proba([user_input])[0][1]
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.error(f"⚠️ Warning: This message is likely a scam.\n\nConfidence: {proba:.2%}")
        else:
            st.success(f"✅ This message looks safe.\n\nConfidence scam: {proba:.2%}")
