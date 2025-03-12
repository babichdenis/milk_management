from django.db import models
from suppliers.models import Supplier


class RawMaterial(models.Model):
    """
    Модель для хранения информации о сырье (молоке).
    """

    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.CASCADE, verbose_name="Поставщик")
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Количество (л)")
    fat_content = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Жирность (%)")
    acidity = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Кислотность")
    received_date = models.DateField(verbose_name="Дата поступления")
    expiration_date = models.DateField(verbose_name="Срок годности")
    document_number = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Номер накладной")
    document_file = models.FileField(
        upload_to='raw_materials/documents/', blank=True, null=True, verbose_name="Файл накладной")

    def __str__(self):
        return f"{self.quantity}L from {self.supplier.name}"
