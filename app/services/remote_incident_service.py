import requests

from app.config import settings


def get_headers():
    return {
        "Authorization": f"Bearer {settings.BEARER_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def create_incident(incident_payload: dict) -> dict:
    """
    Crée un incident sur la plateforme de monitoring distante.
    """
    payload = {
        "title": incident_payload["title"],
        "description": incident_payload["description"],
        "application_id": settings.APPLICATION_ID,
        "status": "OPEN",
        "severity": incident_payload["severity"],
        "start_date": incident_payload["start_date"],
    }

    try:
        response = requests.post(
            settings.INCIDENTS_ENDPOINT,
            json=payload,
            headers=get_headers(),
            timeout=settings.HTTP_TIMEOUT,
        )

        response.raise_for_status()
        data = response.json()

        # On essaie d'extraire l'incident selon plusieurs formats possibles
        if isinstance(data, dict):
            if "data" in data and isinstance(data["data"], dict):
                return data["data"]
            return data

        raise Exception("Invalid incident response format")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to create remote incident: {str(e)}")


def get_incidents() -> dict:
    """
    Récupère les incidents depuis la plateforme distante.
    """
    try:
        response = requests.get(
            settings.INCIDENTS_ENDPOINT,
            headers=get_headers(),
            timeout=settings.HTTP_TIMEOUT,
        )

        response.raise_for_status()
        data = response.json()

        if isinstance(data, dict):
            if "data" in data:
                return data
            return {"data": data}

        return {"data": []}

    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to fetch remote incidents: {str(e)}")