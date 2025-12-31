
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.client_list, name='client_list'),
    path('new/', views.client_create, name='client_create'),
    path('edit/<int:pk>/', views.client_update, name='client_update'),
    path('delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('search/', views.client_search, name='client_search'),
]
