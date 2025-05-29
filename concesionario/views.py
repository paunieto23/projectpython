from django.shortcuts import render, get_object_or_404
from .models import Car, Dealer, Tag

def index(request):
    cars = Car.objects.order_by('-created_at')[:3]
    return render(request, 'index.html', {'cars': cars})

def car_list(request):
    cars = Car.objects.order_by('-created_at')
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    return render(request, 'car_detail.html', {'car': car})

def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, 'dealer_list.html', {'dealers': dealers})

def dealer_detail(request, slug):
    dealer = get_object_or_404(Dealer, slug=slug)
    return render(request, 'dealer_detail.html', {'dealer': dealer})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

def tag_car_list(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    cars = tag.car_set.order_by('-created_at')
    return render(request, 'tag_car_list.html', {'tag': tag, 'cars': cars})
