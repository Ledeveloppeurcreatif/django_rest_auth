from django.db import models
from django.conf import settings
from django.utils import timezone

class Mission(models.Model):
    STATUS_CHOICES = [
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
        ('en_attente', 'En attente'),
        ('termine', 'Terminé'),
    ]

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="missions/")
    titre = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='missions',
        default=1
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    categories = models.ManyToManyField('Categorie', related_name='missions', blank=True)

    def __str__(self):
        return self.titre
    

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="categories/")
    titre = models.CharField(max_length=255)

    def __str__(self):
        return self.titre

    

# class Signalement(models.Model):
#     id = models.AutoField(primary_key=True)
#     cause = models.CharField(max_length=255)
#     description = models.TextField()
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='signalements')
#     mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='signalements')

#     def __str__(self):
#         return self.cause
