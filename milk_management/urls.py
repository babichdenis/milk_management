from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('raw-materials/', include('raw_materials.urls')),  # URL для сырья
    path('products/', include('products.urls')),  # URL для продукции
    # URL для планов производства
    path('suppliers/', include('suppliers.urls')),
    path('production-plans/', include('production_plans.urls')),
    # Главная страница (дашборд)
    path('dashboard/', include('dashboard.urls')),
]
