# Generated by Django 3.1.2 on 2020-10-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='middle_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Отчество'),
        ),
    ]
