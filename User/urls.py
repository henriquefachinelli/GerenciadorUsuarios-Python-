from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    #path('<str:grupo>/', views.HomeEmpresa.as_view(), name=''),
    path('EQUIPE/', views.HomeEQUIPE.as_view(), name='EQUIPE'),
    path('FCB/', views.HomeFCB.as_view(), name='FCB'),
    path('GALERIA/', views.HomeGALERIA.as_view(), name='GALERIA'),
    path('DPZT/', views.HomeDPZT.as_view(), name='DPZT'),
]