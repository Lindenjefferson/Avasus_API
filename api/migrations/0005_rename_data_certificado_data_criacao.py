# Generated by Django 4.1.2 on 2022-11-06 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_certificado_assinado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='data',
            new_name='data_criacao',
        ),
    ]
