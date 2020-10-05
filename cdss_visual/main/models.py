from django.db import models

# Create your models here.


class Patients(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"