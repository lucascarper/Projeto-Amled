from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.client_list, name='list'),
    path('novo/', views.create_client, name='create'),
    path('editar/<int:pk>/', views.edit_client, name='edit'),
    path('excluir/<int:pk>/', views.delete_client, name='delete'),
    path('avaliar/<int:client_pk>/', views.create_avaliacao, name='avaliar'),
]
