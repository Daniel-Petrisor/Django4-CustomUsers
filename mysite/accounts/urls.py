from django.urls import path

from . import views

urlpatterns = [
     # Pagina di registrazione
    path('register/', views.register, name='register'),

    # Pagina di accesso
    path('login/', views.login, name='login'),
]