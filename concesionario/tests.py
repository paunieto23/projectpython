"""
tests.py

Aquest mòdul conté proves unitàries per als models i vistes de l'aplicació 'concesionario'.

Inclou:
- ModelTests: Comprova que els mètodes __str__ dels models funcionin correctament.
- ViewTests: Comprova que les vistes 'index' i 'cars-list' responguin correctament i mostrin les dades esperades.
"""

from django.test import TestCase
from .models import Dealer, Tag, Car
from django.urls import reverse

class ModelTests(TestCase):
    """
    Proves per als models Dealer, Tag i Car.
    """

    def setUp(self):
        self.dealer = Dealer.objects.create(name='Test Dealer')
        self.tag = Tag.objects.create(name='Test Tag')
        self.car = Car.objects.create(title='Test Car', description='Desc', price=10000, dealer=self.dealer)
        self.car.tags.add(self.tag)

    def test_dealer_str(self):
        """Comprova que la representació en text del Dealer sigui correcta."""
        self.assertEqual(str(self.dealer), 'Test Dealer')

    def test_tag_str(self):
        """Comprova que la representació en text del Tag sigui correcta."""
        self.assertEqual(str(self.tag), 'Test Tag')

    def test_car_str(self):
        """Comprova que la representació en text del Car sigui correcta."""
        self.assertEqual(str(self.car), 'Test Car')

class ViewTests(TestCase):
    """
    Proves per a les vistes de l'aplicació.
    """

    def setUp(self):
        self.dealer = Dealer.objects.create(name='Dealer1')
        self.tag = Tag.objects.create(name='Tag1')
        for i in range(5):
            car = Car.objects.create(title=f'Car{i}', description='Desc', price=5000+i, dealer=self.dealer)
            car.tags.add(self.tag)

    def test_index_view(self):
        """Comprova que la vista 'index' respon correctament i mostra 3 cotxes."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('cars' in response.context)
        self.assertEqual(len(response.context['cars']), 3)

    def test_car_list_view(self):
        """Comprova que la vista 'cars-list' mostra tots els cotxes."""
        response = self.client.get(reverse('cars-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cars']), 5)
