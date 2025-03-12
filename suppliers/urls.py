from django.urls import path
from . import views

app_name = 'suppliers'

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('create/', views.supplier_create, name='create'),
    path('update/<int:pk>/', views.supplier_update, name='update'),
    path('delete/<int:pk>/', views.supplier_delete, name='delete'),
]
