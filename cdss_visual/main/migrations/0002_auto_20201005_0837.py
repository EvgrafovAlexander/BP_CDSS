# Generated by Django 3.1.2 on 2020-10-05 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TableFirst',
            new_name='Patients',
        ),
        migrations.AlterModelOptions(
            name='patients',
            options={'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
    ]
