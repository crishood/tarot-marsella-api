from unicodedata import name
from django.db import models

class Card(models.Model):
    KIND = [
        ('Arcano Mayor', 'Arcano Mayor'),
        ('Arcano Menor', 'Arcano Menor'),
    ]
    SUIT = [
        ('Espadas', 'Espadas'),
        ('Copas', 'Copas'),
        ('Oros', 'Oros'),
        ('Bastos', 'Bastos'),
        ('Triunfo', 'Triunfo')
    ]
    name = models.CharField(max_length=100, unique=True)
    picture = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=4000)
    meaning = models.CharField(max_length=4000)
    kind = models.CharField(max_length=20, choices=KIND)
    suit = models.CharField(max_length=20, choices=SUIT)

    def __str__(self):
        return self.name
