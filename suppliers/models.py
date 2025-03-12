from django.db import models
# from raw_materials.models import RawMaterial


class Supplier(models.Model):
    """
    Модель для хранения информации о поставщиках.
    """
    name = models.CharField(max_length=100, verbose_name="Название поставщика")
    contact_person = models.CharField(
        max_length=100, verbose_name="Контактное лицо")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.name
