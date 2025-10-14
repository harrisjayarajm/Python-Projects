import streamlit as st
import random
import time

st.title("🏥 Hospital Sensor Live Monitoring")
st.write("Simulating live sensor data: Heart Rate, Temperature, Oxygen Level")

# Initialize placeholders
heart_rate_bar = st.progress(0)
temperature_bar = st.progress(0)
oxygen_bar = st.progress(0)

heart_rate_text = st.empty()
temperature_text = st.empty()
oxygen_text = st.empty()

# Simulate live updates for 30 seconds (you can increase this)
for _ in range(30):
    hr = random.randint(60, 100)
    temp = round(random.uniform(97.0, 100.0), 1)
    ox = random.randint(90, 100)

    # Update progress bars
    heart_rate_bar.progress(hr)
    temperature_bar.progress(int((temp - 97) / 3 * 100))
    oxygen_bar.progress(ox)

    # Update text displays
    heart_rate_text.text(f"❤️ Heart Rate: {hr} bpm")
    temperature_text.text(f"🌡️ Temperature: {temp} °F")
    oxygen_text.text(f"🫁 Oxygen Level: {ox}%")

    # Wait before updating
    time.sleep(1)
