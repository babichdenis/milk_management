from django.db import models


class Product(models.Model):
    """
    Модель для хранения информации о продукции.
    """
    name = models.CharField(max_length=100, verbose_name="Название")
    volume = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Объем (л/кг)")
    expiration_date = models.DateField(verbose_name="Срок годности")
    production_cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Себестоимость")
    category = models.CharField(max_length=50, verbose_name="Категория")

    def __str__(self):
        return self.name

    def calculate_cost(self, raw_material_cost, additional_costs):
        """
        Метод для расчета себестоимости продукции.
        """
        self.production_cost = raw_material_cost + additional_costs
        self.save()
