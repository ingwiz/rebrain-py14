# Generated by Django 3.2.5 on 2021-07-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='server_is_active',
            field=models.BooleanField(default=False, verbose_name='server_is_active'),
        ),
    ]