# Generated by Django 3.1.14 on 2022-07-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='manzil',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
