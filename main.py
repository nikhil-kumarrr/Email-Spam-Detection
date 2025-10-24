import streamlit as st
import pickle
import numpy as np
from glob import glob

# --- Page setup ---
st.set_page_config(page_title="Email Spam Detection", layout="centered")

# --- Custom CSS for Professional Look ---
st.markdown("""
<style>
/* Smooth gradient background */
.stApp {
    background: linear-gradient(to bottom right, #f8f4ff, #e8ddff);
    font-family: 'Poppins', sans-serif;
}

/* Title styling */
.title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    color: #5a189a;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #4b4b4b;
    margin-bottom: 30px;
}

/* Button styling */
.stButton>button {
    background-color: #7b2cbf;
    color: white;
    border-radius: 10px;
    padding: 12px 35px;
    font-size: 18px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #5a189a;
    transform: scale(1.05);
}

/* Text area styling */
textarea {
    border-radius: 12px !important;
    border: 1px solid #bba8ff !important;
    background-color: #f9f7ff !important;
    color: #2d2d2d !important;
}

/* Prediction box (glassmorphism style) */
.pred-box {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    color: white;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

/* Footer */
footer {
    text-align: center;
    font-size: 14px;
    color: #666;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# --- Title and description ---
st.markdown("<div class='title'>Email Spam Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Classify emails as Spam or Safe using Machine Learning</div>", unsafe_allow_html=True)

# --- Load Model and Vectorizer ---
def load_model_files():
    model_files = glob("*model*.pkl")
    vec_files = glob("*feature*.pkl")

    if not model_files:
        st.error("Model file not found. Example: `Email Spam model.pkl`.")
        return None, None
    if not vec_files:
        st.error("Vectorizer file not found. Example: `feature_extraction.pkl`.")
        return None, None

    try:
        with open(model_files[0], "rb") as f:
            model = pickle.load(f)
        with open(vec_files[0], "rb") as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except Exception as e:
        st.error(f"Error loading files: {e}")
        return None, None

model, vectorizer = load_model_files()

# --- Input section ---
if model and vectorizer:
    email_text = st.text_area("Enter Email Content", height=200, placeholder="Paste or type your email text here...")

    if st.button("Detect Spam"):
        if email_text.strip() == "":
            st.warning("Please enter an email to analyze.")
        else:
            try:
                input_data = vectorizer.transform([email_text])
                prediction = model.predict(input_data)[0]

                if prediction == 1:
                    result = "Not Spam (Safe Email)"
                    color = "#00b894"
                else:
                    result = "🚨 Spam Email Detected"
                    color = "#d00000"

                st.markdown(
                    f"<div class='pred-box' style='background-color:{color};'>{result}</div>",
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"Error during prediction: {e}")