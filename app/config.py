import os
from dotenv import  load_dotenv

#charger le fichier .env

class Settings:
    # API Monitoring externe
    URL_API_MONITORING: str = os.getenv(
        "URL_API_MONITORING",
        "https://monitoring-app.on-forge.com/api"
    )

    INCIDENTS_ENDPOINTS: str = f"{URL_API_MONITORING}/incidents"

    # Authentification
    BEARER_TOKEN: str = os.getenv("BEARER_TOKEN", "")
    APPLICATION_ID: str = os.getenv("APPLICATION_ID", "")


    # Seuil d'alerte
    ALERT_THRESHOLD: int = int(os.getenv("ALERT_THRESHOLD", 30))

    # Timeout HTTP
    HTTP_TIMEOUT: int = int(os.getenv("HTTP_TIMEOUT", 5))

    # ENV
    ENV: str = os.getenv("ENV", "dev")

# Instance globale
settings = Settings()

