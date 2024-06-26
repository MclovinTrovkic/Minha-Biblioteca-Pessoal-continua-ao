
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('livros-por-usuario/', views.livros_por_usuario, name='livros_por_usuario'),
    path('livros-por-autor/<int:autor_id>/', views.livros_por_autor, name='livros_por_autor'),
    path('livros-por-categoria/<int:categoria_id>/', views.livros_por_categoria, name='livros_por_categoria'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
