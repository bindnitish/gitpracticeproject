from pathlib import Path
import sys

# =====================================
# Project Root
# =====================================
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# =====================================
# Imports
# =====================================
import streamlit as st
import tempfile

from inference.predict_crop import predict_crop
from inference.predict_weather import predict_weather
from agent.agent import SmartAgricultureAgent

# =====================================
# Page Configuration
# =====================================
st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌾",
    layout="wide"
)

# =====================================
# Sidebar
# =====================================

st.sidebar.title("🌾 Smart Agriculture")

st.sidebar.markdown("---")

st.sidebar.header("📋 Project")

st.sidebar.write("""
Smart Agriculture AI

• 🌾 Crop Classification

• 🌦 Weather Classification

• 🤖 Agentic AI

• 📡 IoT Simulation
""")

st.sidebar.markdown("---")

st.sidebar.header("👨‍💻 Developer")

st.sidebar.write("**Nitish Kumar Bind**")
st.sidebar.write("M.Tech CSE")
st.sidebar.write("IIIT Naya Raipur")

st.sidebar.markdown("---")

st.sidebar.header("📊 Model Status")

st.sidebar.success("✅ Crop Model")
st.sidebar.success("✅ Weather Model")
st.sidebar.success("✅ Agentic AI")
st.sidebar.success("✅ IoT Simulation")

# =====================================
# Title
# =====================================
st.title("🌾 Smart Agriculture AI System")
st.markdown("### Deep Learning + Agentic AI + IoT")

st.divider()

# =====================================
# Upload Section
# =====================================
col1, col2 = st.columns(2)

with col1:
    crop_image = st.file_uploader(
        "🌾 Upload Crop Image",
        type=["jpg", "jpeg", "png"]
    )

with col2:
    weather_image = st.file_uploader(
        "🌦 Upload Weather Image",
        type=["jpg", "jpeg", "png"]
    )

# =====================================
# Image Preview
# =====================================
col3, col4 = st.columns(2)

with col3:
    if crop_image is not None:
        st.image(
            crop_image,
            caption="Uploaded Crop Image",
            use_container_width=True
        )

with col4:
    if weather_image is not None:
        st.image(
            weather_image,
            caption="Uploaded Weather Image",
            use_container_width=True
        )

st.divider()

# =====================================
# Predict Button
# =====================================
predict = st.button("🚀 Predict")

# =====================================
# Variables
# =====================================
crop_prediction = None
weather_prediction = None
decision = None

# =====================================
# Prediction
# =====================================
st.subheader("📊 Prediction Results")

if predict:

    if crop_image is None or weather_image is None:

        st.warning("⚠ Please upload both images.")

    else:

        # -------------------------------
        # Save Crop Image
        # -------------------------------
        crop_temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        )

        crop_temp.write(crop_image.read())
        crop_temp.close()

        # -------------------------------
        # Save Weather Image
        # -------------------------------
        weather_temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        )

        weather_temp.write(weather_image.read())
        weather_temp.close()

        # -------------------------------
        # AI Prediction
        # -------------------------------
        crop_prediction = predict_crop(crop_temp.name)
        weather_prediction = predict_weather(weather_temp.name)

        # -------------------------------
        # Display Prediction
        # -------------------------------
        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.success(f"🌾 Crop Prediction : {crop_prediction}")

        with result_col2:
            st.success(f"🌦 Weather Prediction : {weather_prediction}")

        # -------------------------------
        # Agent Decision
        # -------------------------------
        agent = SmartAgricultureAgent()

        decision = agent.run(
            crop_prediction,
            weather_prediction
        )

# =====================================
# Agent Decision
# =====================================
st.divider()

st.subheader("🤖 Agentic AI Decision")

if decision is not None:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(f"💧 Irrigation : {decision['irrigation']}")

    with col2:
        st.success(f"🌱 Fertilizer : {decision['fertilizer']}")

    with col3:
        st.success(f"📢 Alert : {decision['action']}")

else:

    st.info("Upload images and click Predict.")

# =====================================
# IoT Status
# =====================================
if decision is not None:

    st.divider()

    st.subheader("📡 IoT System Status")

    col1, col2, col3 = st.columns(3)

    with col1:

        if decision["irrigation"] == "ON":

            st.success("💧 Pump Status : ON")

        else:

            st.error("🚫 Pump Status : OFF")

    with col2:

        st.info(
            f"🌱 Fertilizer Status : {decision['fertilizer']}"
        )

    with col3:

        st.warning(
            f"📢 Farmer Alert : {decision['action']}"
        )

# =====================================
# Footer
# =====================================
st.divider()

st.caption(
    "Smart Agriculture AI | Deep Learning + Agentic AI + IoT"
)