from unicodedata import name
from django.db import models

class Card(models.Model):
    KIND = [
        ('MA', 'Arcano Mayor'),
        ('MI', 'Arcano Menor'),
    ]
    SUIT = [
        ('ES', 'Espadas'),
        ('CO', 'Copas'),
        ('OR', 'Oros'),
        ('BA', 'Bastos'),
    ]
    name = models.CharField(max_length=100, unique=True)
    picture = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=2000)
    meaning = models.CharField(max_length=2000)
    kind = models.CharField(max_length=2, choices=KIND)
    suit = models.CharField(max_length=2, choices=SUIT)

    def __str__(self):
        return self.name
