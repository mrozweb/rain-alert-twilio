import requests
import os
from twilio.rest import Client

# ========== OPENWEATHER API ==========
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = 52.018785
MY_LONG = 5.169937

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)
response.raise_for_status()
weather_data = response.json()

# ========== TWILIO SETUP ==========
# Add your Twilio credentials
TWILIO_ACCOUNT_SID = os.environ.get("ACCOUNT_SID")  # From Twilio Dashboard
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")    # From Twilio Dashboard
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_NR")  # Twilio Sandbox number
YOUR_WHATSAPP_NUMBER = os.environ.get("MY_VERIFIED_NR")     # Your verified number

# Create Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# ========== CHECK FOR RAIN ==========
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

# ========== SEND WHATSAPP MESSAGE ==========
if will_rain:
    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body="🌧️ It's going to rain today. Remember to bring an umbrella! ☂️",
            to=YOUR_WHATSAPP_NUMBER
        )
        print(f"WhatsApp message sent!")
        print(f"Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")
