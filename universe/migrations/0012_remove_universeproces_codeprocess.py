# Generated by Django 4.0.1 on 2022-01-25 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0011_alter_universemacroproces_codemacro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universeproces',
            name='codeProcess',
        ),
    ]