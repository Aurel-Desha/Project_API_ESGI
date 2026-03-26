* PREREQUIS 

* * - Installation de Python
* * - Installation des module avec la commande pip install -r requirements.txt
        fastapi : Créer une API rapidement (routes, endpoints, JSON)
        uvicorn : Serveur qui lance notre app FastAPI
        psutil  : Récupérer les information du système (CPU, RAM, disque, etc.)
        requests: Faire des appels HTTP (GET, POST…)
        python-dotenv: Charger les variables depuis un fichier .env


* Lancer l'appli: 
python -m uvicorn app.main:app --reload

* ARCHITECTURE 
Architecture MVC


                    monitoring-api/ 
                    │ ├── app/ 
                    │ ├── main.py 
                    │ ├── config.py 
                    │ ├── routes/ 
                    │ │ └── monitoring.py 
                    │ ├── services/ 
                    │ │ ├── system_service.py 
                    │ │ ├── alert_service.py 
                    │ │ └── incident_service.py 
                    │ ├── models/ 
                    │ │ ├── responses.py 
                    │ │ └── errors.py 
                    │ └── utils/ 
                    │ └── datetime_helper.py 
                    │ ├── .env 
                    ├── requirements.txt 
                    ├── README.md

    app: C'est le dossier pricipal du projet
    routes: sert à centraliser et organiser la définition des endpoints (URLs).
    services: C'est l'endroit où on implémente ce que l'application fait vraiment :


