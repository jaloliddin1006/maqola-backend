# Generated by Django 3.1.14 on 2022-07-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_manzil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='manzil',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
