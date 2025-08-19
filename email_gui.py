# email_gui.py

import streamlit as st
import joblib
from suspicious_words import suspicious_words  # Import from external file

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit page setup
st.set_page_config(page_title="PhishShield - Email Detector", layout="centered")

st.title("🛡️ PhishShield – Email Classifier with AI Brain")
st.markdown("Enter your email content below to check if it's **Phishing** or **Safe**.")

# Text input
email_text = st.text_area("📧 Email Content", height=200)

if st.button("🔍 Detect"):
    if not email_text.strip():
        st.warning("⚠️ Please enter some email content!")
    else:
        # Transform input and predict
        email_vector = vectorizer.transform([email_text])
        prediction = model.predict(email_vector)[0]
        probability = model.predict_proba(email_vector)[0]
        
        # Output
        label = "🚨 Phishing Email" if prediction == 1 else "✅ Safe Email"
        confidence = max(probability) * 100

        st.markdown(f"### 🔎 Result: **{label}**")
        st.markdown(f"#### 📊 Confidence: `{confidence:.2f}%`")

        # Highlight suspicious words from external list
        matches = [word for word in suspicious_words if word.lower() in email_text.lower()]
        if matches:
            st.markdown(f"🔴 **Suspicious Words Found:** `{', '.join(matches)}`")
        else:
            st.markdown("🟢 No suspicious words detected.")
