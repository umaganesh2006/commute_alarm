import streamlit as st
import time
from datetime import datetime, timedelta
import api_handler  # This is your existing file with TomTom logic!

# 1. Page Config (Tab Title & Icon)
st.set_page_config(page_title="Commute Alarm", page_icon="⏰")

# 2. The UI Layout
st.title("🚗 Commute-Aware Alarm")
st.write("Calculates your wake-up time based on **Real-Time Traffic & Weather**.")

# 3. User Inputs
col1, col2 = st.columns(2)
with col1:
    target_time = st.time_input("Target Arrival Time", value=datetime.strptime("09:00", "%H:%M").time())
with col2:
    prep_time = st.number_input("Prep Time (mins)", min_value=15, max_value=120, value=45)

# 4. The "Calculate" Button
if st.button("Set Alarm & Calculate"):
    with st.spinner("Checking traffic with TomTom..."):
        # Fetch Real Data
        traffic_min = api_handler.get_commute_duration()
        weather_status = api_handler.get_weather_status()
        
        # Calculate Buffer
        weather_buffer = 0
        if weather_status in ["Snow", "Rain", "Thunderstorm", "Drizzle"]:
            weather_buffer = 15
            st.warning(f"🌧️ Bad Weather ({weather_status}) detected! Added 15 min buffer.")
        else:
            st.success(f"☀️ Weather looks good ({weather_status}). No extra buffer.")

        # Total Calculation
        total_deduction = traffic_min + prep_time + weather_buffer
        
        # Convert Target Time to DateTime to do math
        now = datetime.now()
        target_dt = datetime.combine(now.date(), target_time)
        
        # If target is earlier than now (e.g. 9 AM tomorrow), add a day
        if target_dt < now:
            target_dt += timedelta(days=1)

        wakeup_dt = target_dt - timedelta(minutes=total_deduction)
        
        # Display Results
        st.divider()
        st.metric(label="🚙 Traffic Delay", value=f"{traffic_min} mins")
        st.metric(label="⏰ You Must Wake Up At", value=wakeup_dt.strftime("%H:%M"))
        
        # 5. The "Alarm" Feature (Browser Limitation)
        # Web browsers block "auto-play" audio unless you interact with them.
        # We show a player the user can click, or a countdown.
        seconds_until_alarm = (wakeup_dt - datetime.now()).total_seconds()
        
        if seconds_until_alarm > 0:
            st.info(f"Alarm set for {wakeup_dt.strftime('%H:%M')}. Keep this tab open!")
            # In a real deployed app, background timers are tricky.
            # For this MVP, we show the data.
        else:
            st.error("You are already late! Go!")
            # Play sound (Works in most browsers if user clicked the button)
            st.audio("assets/alarm_sound.mp3", format="audio/mp3", autoplay=True)