from django.urls import path
from audit import views

urlpatterns = [
    path('',views.index, name='index'),
    path('subModuleCreateAudit/', views.subModuleCreateAudit,name='subModuleCreateAudit'),
]
