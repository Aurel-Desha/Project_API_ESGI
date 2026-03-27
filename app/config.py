import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONITORING_API_URL = os.getenv("MONITORING_API_URL", "https://monitoring-app.on-forge.com/api")
    INCIDENTS_ENDPOINT = f"{MONITORING_API_URL}/incidents"
    BEARER_TOKEN = os.getenv("BEARER_TOKEN", "").strip()
    APPLICATION_ID = os.getenv("APPLICATION_ID", "").strip()
    ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD", 30))
    HTTP_TIMEOUT = int(os.getenv("HTTP_TIMEOUT", 5))

settings = Settings()

