from django.db import models
from django.utils import timezone

# Create your models here.
class Przedmiot(models.Model):
    nazwa = models.TextField()
    cena = models.IntegerField()
    ilosc = models.IntegerField()
    dodal = models.ForeignKey('auth.User',on_delete = models.CASCADE)

    def dodaj(self):
        self.data_dodania = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa
