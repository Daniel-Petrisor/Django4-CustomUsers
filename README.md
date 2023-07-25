# Guida introduttiva

Questo documento è una guida alla creazione di un nuovo progetto django che utilizza:
1. Python 3.9.10
1. virtualenv
1. pip
1. Django 4.2.3 (LTS)


## 1. Preparazione dell'ambiente virtuale (virtualenv):
Assicurati di avere Python installato sul tuo sistema, oppure installa Python
https://www.python.org/downloads/release/python-3910/

1. Crea una cartella per il progetto
    - Esempio: `D://DjangoProjects/`

1. Crea e attiva l'ambiente virtuale (virtualenv)
    - Vai nella cartella del progetto, apri il terminale CMD e utilizza il comando
    - `python -m venv venv`

1. Naviga nella cartella 'venv'. Utilizza il comando
    - `cd venv`

1. Attivare l'ambiente virtuale. Utilizza il comando
    - **Windows**: `Scripts\activate` 
	- **Linux**: `source bin/activate`
	- **Mac (I think)**: `source bin/activate`


## 2. Installa Django e crea un nuovo progetto:
1. Installa Django utilizzando il package manager di Python (pip).
    - `pip install django==4.2.3`

1. Installa libreria crispy-bootstrap5 (opzionale)
    - `pip install crispy-bootstrap5==0.7`

1. Naviga nella cartella `D://DjangoProjects/`. Utilizza il comando
    - `cd ..`

1. Crea un nuovo progetto Django. Utilizza il comando
    - `django-admin startproject mysite`

1. Naviga nella cartella `D://DjangoProjects/mysite`. Utilizza il comando
    - `cd mysite`

1. Tieni traccia delle librerie che usi. Utilizza il comando ogni volta che installi nuove librerie
    - `pip freeze > requirements.txt`

1. Esegui il server per assicurarti che funzioni
    - `python manage.py runserver`

1. Visita `http://127.0.0.1:8000/`
**Hai avviato il server di sviluppo Django**

https://docs.djangoproject.com/it/4.2/intro/tutorial01/
