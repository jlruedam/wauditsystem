from django.urls import path
from universe import views

urlpatterns = [
    path('prueba/',views.prueba),
    path('universe/',views.universeAudit, name='universeAudit'),
]
