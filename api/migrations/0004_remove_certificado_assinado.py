# Generated by Django 4.1.2 on 2022-11-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_professor_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificado',
            name='assinado',
        ),
    ]