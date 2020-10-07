# Generated by Django 3.1.2 on 2020-10-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201005_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteBloodCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cbc', models.DateField(verbose_name='Дата анализа')),
                ('rbc_cbc', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='Эритроциты')),
                ('hb_cbc', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='Гемоглобин')),
                ('wbc_cbc', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='Лейкоциты')),
            ],
        ),
    ]