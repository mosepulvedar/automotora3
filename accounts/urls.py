from django.urls import path
from .views import register, cambiar_pass
urlpatterns = [
    path('register/', register, name="register"),
    path('cambiar-password/', cambiar_pass, name="cambiar_pass"),
]
