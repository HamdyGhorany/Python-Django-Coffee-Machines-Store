# Generated by Django 3.1.1 on 2020-09-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_auto_20200914_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]