"""
models.py

Aquest mòdul defineix els models de dades per a l'aplicació 'concesionario'.

Inclou:
- Dealer: Representa un concessionari de vehicles.
- Tag: Representa una etiqueta per classificar vehicles.
- Car: Representa un vehicle en venda, associat a un concessionari i etiquetes.
"""

from django.db import models
from django.utils.text import slugify

class Dealer(models.Model):
    """
    Model que representa un concessionari de vehicles.

    Camps:
    - name: Nom del concessionari.
    - slug: Identificador únic amigable per a URL, generat automàticament a partir del nom.
    - bio: Descripció opcional del concessionari.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bio = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    Model per a etiquetes que es poden assignar als vehicles.

    Camps:
    - name: Nom de l'etiqueta (únic).
    - slug: Identificador únic amigable per a URL, generat automàticament.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Car(models.Model):
    """
    Model que representa un vehicle disponible a la venda.

    Camps:
    - title: Títol o nom del vehicle.
    - slug: Identificador únic amigable per a URL, generat automàticament.
    - description: Descripció del vehicle.
    - price: Preu del vehicle.
    - dealer: Concessionari que ofereix el vehicle.
    - tags: Etiquetes associades (opcionales).
    - image: Imatge del vehicle (opcional).
    - created_at: Data de creació del registre.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='cars')
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
