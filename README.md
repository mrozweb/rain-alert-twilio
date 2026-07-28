# 🌧️ Rain Alert System

A Python-based weather alert system that automatically sends you a WhatsApp message when rain is expected in your location.

## ✨ Features

- 🌤️ **Real-time weather checks** using OpenWeatherMap API
- 📱 **WhatsApp notifications** via Twilio
- ⏰ **Automated daily checks** using GitHub Actions
- 🔒 **Secure credential management** with GitHub Secrets
- 🛠️ **Manual trigger** option for testing

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [OpenWeatherMap API key](https://home.openweathermap.org/api_keys)
- [Twilio Account](https://www.twilio.com/try-twilio) with WhatsApp Sandbox enabled
- GitHub account

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/rain-alert-twilio.git
cd rain-alert-twilio
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:

```env
OWM_API_KEY=your_openweather_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
YOUR_WHATSAPP_NUMBER=whatsapp:+your_verified_number
```

5. **Run the script locally**

```bash
python main.py
```

## ⚙️ GitHub Actions Setup

1. **Create a repository** and push this code
2. **Add GitHub Secrets**:
   - Go to **Settings → Secrets and variables → Actions**
   - Add the following secrets:

| Secret Name | Description |
|-------------|-------------|
| `OWM_API_KEY` | Your OpenWeatherMap API key |
| `TWILIO_ACCOUNT_SID` | Your Twilio Account SID |
| `TWILIO_AUTH_TOKEN` | Your Twilio Auth Token |
| `TWILIO_WHATSAPP_NUMBER` | Your Twilio WhatsApp number |
| `YOUR_WHATSAPP_NUMBER` | Your verified WhatsApp number |

3. **The workflow will run automatically** at 9:00 AM UTC daily

## 📁 Project Structure

```
rain-alert-twilio/
├── .github/
│   └── workflows/              # GitHub Actions workflow
│       └── scheduled.yml    
|       └── test.yml
├── main.py                     # Main application script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## 🔧 Customization

### Change Check Time

Edit the cron schedule in `.github/workflows/scheduled.yml`:

```yaml
- cron: '0 9 * * *'  # Change to your preferred time (UTC)
```

### Change Location

Update the coordinates in `main.py`:

```python
MY_LAT = 52.018785   # Your latitude
MY_LONG = 5.169937   # Your longitude
```

### Change Message

Modify the WhatsApp message in `main.py`:

```python
body="🌧️ It's going to rain today. Remember to bring an umbrella! ☂️"
```

## 📝 Environment Variables

| Variable | Description |
|----------|-------------|
| `OWM_API_KEY` | OpenWeatherMap API key |
| `TWILIO_ACCOUNT_SID` | Twilio Account SID |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token |
| `TWILIO_WHATSAPP_NUMBER` | Twilio WhatsApp number (e.g., `whatsapp:+14155238886`) |
| `YOUR_WHATSAPP_NUMBER` | Your verified WhatsApp number (e.g., `whatsapp:+3162234523`) |

## 🛠️ Technologies Used

- [Python 3.12](https://www.python.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Twilio WhatsApp API](https://www.twilio.com/whatsapp)
- [GitHub Actions](https://github.com/features/actions)
- [Requests](https://docs.python-requests.org/) for API calls

## 📧 Contact

For any questions or suggestions, please open an issue or contact the maintainer.

**Made with ❤️ and Python**
