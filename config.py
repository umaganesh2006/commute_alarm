# config.py

# ==========================================
# 1. API KEYS (We will get these next!)
# ==========================================
# Get this from: https://console.cloud.google.com/
try:
    TOMTOM_API_KEY = st.secrets["TOMTOM_API_KEY"]
except:
    # Fallback for local testing if secrets aren't set up locally
    TOMTOM_API_KEY = "YOUR_REAL_KEY_HERE"
# Get this from: https://openweathermap.org/api
OPENWEATHER_API_KEY = "ec8fe1875ab6a4d2d3f9cf0e757af597"

# ==========================================
# 2. LOCATIONS
# ==========================================
# Be as specific as possible to get accurate traffic data
HOME_ADDRESS = "Times Square, New York, NY" 
WORK_ADDRESS = "Central Park Zoo, New York, NY"

# ==========================================
# 3. TIME SETTINGS
# ==========================================
# What time do you absolutely need to walk through the office door? (24-hour format)
TARGET_ARRIVAL_TIME = "18:00"

# How many minutes do you need to shower, eat, and get ready?
PREP_TIME_MINUTES = 45

# If the internet is down or APIs fail, what is the safe backup wake-up time?
DEFAULT_WAKEUP_TIME = "07:30"

# ==========================================
# 4. WEATHER RULES
# ==========================================
# If it's snowing or raining, how many EXTRA minutes of buffer do you want?
BAD_WEATHER_BUFFER_MINUTES = 15
