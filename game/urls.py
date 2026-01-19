from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('play/', views.game_view, name='game'),
    path('api/cards/', views.get_cards_api, name='get_cards'),
    path('api/save_score/', views.save_score_api, name='save_score'),
]
