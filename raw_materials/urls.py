from django.urls import path
from . import views

app_name = 'raw_materials'

urlpatterns = [
    path('', views.raw_material_list, name='raw_material_list'),
    path('create/', views.raw_material_create, name='create'),
    path('update/<int:pk>/', views.raw_material_update, name='update'),
    path('delete/<int:pk>/', views.raw_material_delete, name='delete'),
]
