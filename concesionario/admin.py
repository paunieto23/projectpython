"""
Registre dels models Dealer, Tag i Car al panell d'administració de Django.
"""

from django.contrib import admin
from .models import Dealer, Tag, Car

admin.site.register(Dealer)
admin.site.register(Tag)
admin.site.register(Car)
