# Generated by Django 3.1.1 on 2020-09-14 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0007_auto_20200914_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffeemachine',
            old_name='product_type_pods',
            new_name='pods_type',
        ),
    ]