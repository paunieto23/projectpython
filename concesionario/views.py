"""
views.py

Conté les vistes de l'aplicació 'concesionario'.

Inclou funcionalitats per:
- Mostrar els cotxes més recents a la pàgina principal.
- Llistar tots els cotxes, concessionaris i etiquetes.
- Mostrar detalls d’un cotxe, d’un concessionari o d’una etiqueta concreta.
"""

from django.shortcuts import render, get_object_or_404
from .models import Car, Dealer, Tag

def index(request):
    """
    Mostra la pàgina principal amb els 3 últims cotxes afegits.
    """
    cars = Car.objects.order_by('-created_at')[:3]
    return render(request, 'index.html', {'cars': cars})

def car_list(request):
    """
    Mostra un llistat de tots els cotxes disponibles.
    """
    cars = Car.objects.order_by('-created_at')
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, slug):
    """
    Mostra els detalls d’un cotxe concret identificat pel seu slug.
    """
    car = get_object_or_404(Car, slug=slug)
    return render(request, 'car_detail.html', {'car': car})

def dealer_list(request):
    """
    Mostra un llistat de tots els concessionaris.
    """
    dealers = Dealer.objects.all()
    return render(request, 'dealer_list.html', {'dealers': dealers})

def dealer_detail(request, slug):
    """
    Mostra els detalls d’un concessionari concret.
    """
    dealer = get_object_or_404(Dealer, slug=slug)
    return render(request, 'dealer_detail.html', {'dealer': dealer})

def tag_list(request):
    """
    Mostra un llistat de totes les etiquetes disponibles.
    """
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

def tag_car_list(request, slug):
    """
    Mostra els cotxes associats a una etiqueta concreta.
    """
    tag = get_object_or_404(Tag, slug=slug)
    cars = tag.car_set.order_by('-created_at')
    return render(request, 'tag_car_list.html', {'tag': tag, 'cars': cars})
