# Generated by Django 4.1.2 on 2022-11-04 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_professor_termo_uso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='senha',
        ),
    ]
