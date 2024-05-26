from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('tekmovanja/', views.tekmovanja, name='tekmovanja'),
    path('porocila/', views.porocila, name='porocila'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
    path('generate_reports/get_runner_results/<str:ironman_name>/<str:ironman_surname>/', views.get_runner_results, name='get_runner_results'),    
    path('generate_reports/get_biker_results/<str:ironman_name>/<str:ironman_surname>/', views.get_biker_results, name='get_biker_results'),    
    path('generate_reports/get_swimmer_results/<str:ironman_name>/<str:ironman_surname>/', views.get_swimmer_results, name='get_swimmer_results'),   
    path('add_objava', views.add_objava, name='add_objava'),
    path('objava_added/<str:title>/<str:body>/<str:author>/<int:upvote>/<int:downvote>/', views.objava_added, name='objava_added'),
    path('translate/<str:lang_code>/', views.translate, name='translate'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout'),
    path('auth', views.auth, name='auth'),

] 
