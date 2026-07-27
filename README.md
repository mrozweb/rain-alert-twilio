🌧️ Rain Alert System
A Python-based weather alert system that automatically sends you a WhatsApp message when rain is expected in your location.

Features
Real-time weather checks using OpenWeatherMap API

WhatsApp notifications via Twilio

Automated daily checks using GitHub Actions

Secure credential management with GitHub Secrets

🛠️ Manual trigger option for testing

🚀 Quick Start
Prerequisites
Python 3.8 or higher

OpenWeatherMap API key

Twilio Account with WhatsApp Sandbox enabled

GitHub account

Installation
Clone the repository

bash
git clone https://github.com/your-username/rain-alert-twilio.git
cd rain-alert-twilio
Create a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables
Create a .env file in the project root:

env
OWM_API_KEY=your_openweather_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
YOUR_WHATSAPP_NUMBER=whatsapp:+your_verified_number
Run the script locally

bash
python main.py
⚙️ GitHub Actions Setup
Fork or create a repository and push this code

Add GitHub Secrets:

Go to Settings → Secrets and variables → Actions

Add the following secrets:

OWM_API_KEY

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

TWILIO_WHATSAPP_NUMBER

YOUR_WHATSAPP_NUMBER

The workflow will run automatically at 9:00 AM UTC daily

📁 Project Structure
text
rain-alert-twilio/
├── .github/
│   └── workflows/
│       └── daily-script.yml    # GitHub Actions workflow
├── main.py                     # Main application script
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation

🔧 Customization
Change Check Time
Edit the cron schedule in .github/workflows/daily-script.yml:

yaml
- cron: '0 9 * * *'  # Change to your preferred time (UTC)
Change Location
Update the coordinates in main.py:

python
MY_LAT = 52.018785   # Your latitude
MY_LONG = 5.169937   # Your longitude
Change Message
Modify the WhatsApp message in main.py:

python
body="🌧️ It's going to rain today. Remember to bring an umbrella! ☂️"
📝 Environment Variables
Variable	Description
OWM_API_KEY	OpenWeatherMap API key
TWILIO_ACCOUNT_SID	Twilio Account SID
TWILIO_AUTH_TOKEN	Twilio Auth Token
TWILIO_WHATSAPP_NUMBER	Twilio WhatsApp number (e.g., whatsapp:+14155238886)
YOUR_WHATSAPP_NUMBER	Your verified WhatsApp number (e.g., whatsapp:+3162234523)

🛠️ Technologies Used
Python 3.12

OpenWeatherMap API

Twilio WhatsApp API

GitHub Actions

Requests for API calls

📧 Contact
For any questions or suggestions, please open an issue or contact the maintaine

Made with ❤️ and Python
