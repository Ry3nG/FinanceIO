from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('app/', include([
        path('', views.dashboard, name='dashboard'),
        path('add_transaction/', views.add_transaction, name='add_transaction'),
        path('logout/', views.logout_view, name='logout'),
    ])),
    path('register/', views.register_view, name='register'),
]
