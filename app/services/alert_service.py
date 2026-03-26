from app.services.remote_incident_service import create_incident
from app.services.system_services import get_health_info
from datetime import datetime


THRESHOLD = 30  # seuil demandé


# =========================
# SEVERITY
# =========================
def get_severity(percent: float) -> str:
    if percent <= 60:
        return "LOW"
    elif percent <= 90:
        return "HIGH"
    else:
        return "CRITICAL"


# =========================
# GENERATE INCIDENT PAYLOAD
# =========================
def build_incident(metric_name: str, value: float):
    host = get_health_info()

    severity = get_severity(value)

    title = f"ALERTE {metric_name.upper()} — Utilisation à {value:.2f}%"
    description = (
        f"Le serveur {host['hostname']} a détecté une utilisation "
        f"{metric_name.upper()} anormale de {value:.2f}% à {host['checked_at']}."
    )

    start_date = datetime.now().isoformat()

    return {
        "title": title,
        "description": description,
        "severity": severity,
        "start_date": start_date
    }


# =========================
# CHECK + TRIGGER ALERT
# =========================
def check_and_alert(metric_name: str, value: float):
    try:
        if value > THRESHOLD:
            incident_payload = build_incident(metric_name, value)

            # appel API distante
            response = create_incident(incident_payload)

            return {
                "alert_triggered": True,
                "incident": {
                    "id": response.get("id"),
                    "severity": incident_payload["severity"],
                    "message": "Incident created on monitoring platform"
                }
            }

        return {
            "alert_triggered": False
        }

    except Exception:
        # si l'API distante échoue → ne pas casser ton API
        return {
            "alert_triggered": True,
            "incident": {
                "id": None,
                "severity": "UNKNOWN",
                "message": "Failed to create incident"
            }
        }