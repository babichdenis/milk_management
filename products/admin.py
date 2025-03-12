from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Административная панель для управления продукцией.
    """
    list_display = ('name', 'volume', 'expiration_date',
                    'production_cost', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category', 'expiration_date')
