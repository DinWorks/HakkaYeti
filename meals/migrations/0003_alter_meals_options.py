# Generated by Django 4.1.2 on 2022-11-10 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meals_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'meal', 'verbose_name_plural': 'meals'},
        ),
    ]
