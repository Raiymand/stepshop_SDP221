# Generated by Django 4.2.5 on 2023-12-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
