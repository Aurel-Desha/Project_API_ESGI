import psutil
import platform
import socket
from datetime import datetime

# Format de date demandé

def get_current_time():
    return datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")

# HEALTH

def get_health_info():
    try:
        return {
            "status": "UP",
            "hostname": socket.gethostname(),
            "os": platform.system().lower(),
            "platform": platform.platform(),
            "checked_at": get_current_time()
        }
    except Exception:
        raise Exception("Impossible de d'obtenir l'état de santé")


# CPU
def get_cpu_info():
    try:
        return {
            "total_usage_percent": psutil.cpu_percent(interval=1),
            "logical_cores": psutil.cpu_count(logical=True),
            "physical_cores": psutil.cpu_count(logical=False),
            "checked_at": get_current_time()
        }
    except Exception:
        raise Exception("Impossible d'afficher le cpu")


#Memory
def get_memory_info():
    try:
        memory: psutil.virtual_memory()

        return {
            "total_gb": round(memory.total / (1024**3)),
            "used_gb": round(memory.used / (1024**3)),
            "free_gb": round(memory.available / (1024**3)),
            "used_percent": memory.percent,
            "checked_at": get_current_time()
        }
    except Exception:
        raise Exception("Impossible d'afficher la memoire")

# ALL
def get_all_metrics():
    try:
        return {
            "host_info": get_health_info(),
            "cpu_info": get_cpu_info(),
            "memory_info": get_memory_info(),
            "disk_info": get_disk_info()
        }
    except Exception:
        raise Exception("Impossible d'afficher tous les metrics")