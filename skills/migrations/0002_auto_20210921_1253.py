# Generated by Django 3.1.13 on 2021-09-21 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['skill']},
        ),
        migrations.AlterModelOptions(
            name='skilltype',
            options={'ordering': ['type']},
        ),
    ]