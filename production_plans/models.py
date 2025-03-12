from django.db import models
from products.models import Product


class ProductionPlan(models.Model):
    """
    Модель для хранения планов производства.
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукция")
    quantity = models.IntegerField(verbose_name="Количество")
    planned_date = models.DateField(verbose_name="Планируемая дата")
    status = models.CharField(
        max_length=20,
        choices=[('planned', 'Запланировано'), ('completed', 'Завершено')],
        default='planned',
        verbose_name="Статус"
    )

    def __str__(self):
        return f"План для {self.product.name} на {self.planned_date}"
