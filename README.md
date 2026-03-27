## Introduction

Nous avons developpé une API Rest qui collecte les Information de certains service de notre machine(Memoire, Cpu, disk,...). De meme, notre API sera capable d'en consommé une autre API pour afficher les incident relatives aux états de nos services.


## PREREQUIS 

*  Installation de Python
*  Installation des module avec la commande pip install -r requirements.txt qui contient tous les module suivant:
    *   fastapi : Créer une API rapidement (routes, endpoints, JSON)
    *   uvicorn : Serveur qui lance notre app FastAPI
    *   psutil  : Récupérer les information du système (CPU, RAM, disque, etc.)
    *   requests: Faire des appels HTTP (GET, POST…)
    *   python-dotenv: Charger les variables depuis un fichier .env
*   Postman: Interface permettant de tester nos requettes

## Lancer l'appli: 
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


