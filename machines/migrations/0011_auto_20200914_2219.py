# Generated by Django 3.1.1 on 2020-09-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0010_auto_20200914_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeepods',
            name='Category',
        ),
        migrations.AddField(
            model_name='coffeemachine',
            name='Category',
            field=models.CharField(blank=True, choices=[('Base', 'Base'), ('Premium', 'Premium'), ('Deluxe', 'Deluxe')], max_length=50),
        ),
    ]
