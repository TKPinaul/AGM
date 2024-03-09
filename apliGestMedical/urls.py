from django.urls import path
from apliGestMedical import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('accueil/<int:user_id>/', views.accueil, name='accueil'),
    path('myCompte/<int:user_id>/', views.myUserCompte, name='MyCompte'),
    path('rendez-vous/<int:user_id>/', views.rendezVous, name='rendezVous'),
    
]