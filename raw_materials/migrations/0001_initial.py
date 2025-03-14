# Generated by Django 5.1.7 on 2025-03-11 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество (л)')),
                ('fat_content', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Жирность (%)')),
                ('acidity', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Кислотность')),
                ('received_date', models.DateField(verbose_name='Дата поступления')),
                ('expiration_date', models.DateField(verbose_name='Срок годности')),
                ('document_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер накладной')),
                ('document_file', models.FileField(blank=True, null=True, upload_to='raw_materials/documents/', verbose_name='Файл накладной')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier', verbose_name='Поставщик')),
            ],
        ),
    ]
