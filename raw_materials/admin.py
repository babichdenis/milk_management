from django.contrib import admin
from .models import RawMaterial


@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'quantity', 'fat_content',
                    'acidity', 'received_date', 'expiration_date')
    search_fields = ('supplier__name', 'document_number')
    list_filter = ('supplier', 'received_date', 'expiration_date')
