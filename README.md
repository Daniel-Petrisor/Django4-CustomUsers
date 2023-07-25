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


## 3. Creazione dell'applicazione Accounts:
1.  Assicurati di essere nella stessa cartella di manage.py 
    `D://DjangoProjects/mysite`

1.  Crea una nuova applicazione "accounts", usa il comando
    - `python manage.py startapp accounts`

1. Apri il file accounts/views.py e scrivi il seguente codice
    ```
    from django.shortcuts import render
    from django.http import HttpResponse

    # Pagina di registrazione
    def register(request):
    return HttpResponse("Pagina di registrazione")

    # Pagina di accesso
    def login(request):
    return HttpResponse("Pagina di accesso")
    ```

1. Crea il file urls.py all'interno dell'applicazione "accounts" e includi il seguente codice
    ```
    from django.urls import path
    from . import views

    urlpatterns = [
        # Pagina di registrazione
        path('register/', views.register, name='register'),

         # Pagina di accesso
        path('login/', views.login, name='login'),
    ]
    ```

1. In mysite/urls.py, aggiungi seguente codice
    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path("", include("accounts.urls")),
    ]
    ```

1. Esegui il server per assicurarti che funzioni
    - `python manage.py runserver`

1. Visita `http://127.0.0.1:8000/register/`
    **Pagina di registrazione**
1. Visita `http://127.0.0.1:8000/login/`
    **Pagina di accesso**

1. crea github commit
    - git status
    - git add -A
    - git commit -m "prima vista applicazione accounts - creazione parziale URL e Views (register; login)"
    - git push origin main



1. Modifica le impostazioni nel file mysite/settings.py del tuo progetto
    - aggiungi all'inizio del file il codice
        `import os`

    - includere l’app nel tuo progetto
        ```
        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",

            "accounts",
        ]
        ```

    - imposta TEMPLATES del tuo progetto
        ```
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```

    - imposta TIME_ZONE sul tuo fuso orario
        ```
        LANGUAGE_CODE = 'it'
        TIME_ZONE = 'Europe/Rome'
        ```
    
    - imposta STATICFILE nel tuo progetto
        ```
        # command: python manage.py collectstatic
        STATIC_ROOT = BASE_DIR / 'staticfiles ' 

        # Definisci la directory per i file statici
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static')
            ]

        # Percorso di base per i media file caricati dagli utenti
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

1. Naviga nella cartella `D://DjangoProjects/mysite`, crea le cartelle
    - statifile
    - static
    - media
    - templates

1. Modifica il file mysite/urls.py del tuo progetto
    ```
    from django.conf import settings
    from django.conf.urls.static import static

    # utilizzando il modulo di servizio statico di Django durante lo sviluppo
    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

1. crea github commit
    - git status
    - git add -A
    - git commit -m "settings.py, urls.py - modifica e implementazione INSTALLED_APPS, TEMPLATES, TIME_ZONE, STATICFILE"
    - git push origin main