# Generated by Django 4.1.3 on 2022-12-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=555),
        ),
    ]
