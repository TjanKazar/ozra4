from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tekmovanja/', views.tekmovanja, name='tekmovanja'),
    path('porocila/', views.porocila, name='porocila'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
    path('generate_reports/get_runner_results/<str:ironman_name>/<str:ironman_surname>/', views.get_runner_results, name='get_runner_results'),    
    path('generate_reports/get_bikers_results/<str:ironman_name>/<str:ironman_surname>/', views.get_runner_results, name='get_runner_results'),    
    path('generate_reports/get_swimmers_results/<str:ironman_name>/<str:ironman_surname>/', views.get_runner_results, name='get_runner_results'),    



] 
