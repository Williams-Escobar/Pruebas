from django.urls import path
from . import views

urlpatterns = [
   path('categorias/', views.categorias, name='categorias'),
   path('update_server/', views.update, name="update"),
   path('categorias/nuevo', views.categoria_nuevo, name='categoria_nuevo'),
   path('categoria/<int:pk>/edit/', views.categoria_edit, name='categoria_edit'),
   path('categoria/<int:pk>/delete/', views.categoria_delete, name='categoria_delete'),
   path('', views.pelicula_list, name='pelicula_list'),
   path('newPelicula', views.create_pelicula, name='create_pelicula'),
   path('edit_pelicula/<int:pk>', views.edit_pelicula, name='edit_pelicula'),
   path('delete_pelicula/<int:pk>', views.delete_pelicula, name='delete_pelicula'),
]

