# Generated by Django 5.0.3 on 2024-04-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDeMiPre', '0005_alter_usuarios_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='rol',
            field=models.CharField(max_length=20),
        ),
    ]
