from django.test import TestCase
from .models import Dealer, Tag, Car
from django.urls import reverse

class ModelTests(TestCase):
    def setUp(self):
        self.dealer = Dealer.objects.create(name='Test Dealer')
        self.tag = Tag.objects.create(name='Test Tag')
        self.car = Car.objects.create(title='Test Car', description='Desc', price=10000, dealer=self.dealer)
        self.car.tags.add(self.tag)

    def test_dealer_str(self):
        self.assertEqual(str(self.dealer), 'Test Dealer')

    def test_tag_str(self):
        self.assertEqual(str(self.tag), 'Test Tag')

    def test_car_str(self):
        self.assertEqual(str(self.car), 'Test Car')

class ViewTests(TestCase):
    def setUp(self):
        self.dealer = Dealer.objects.create(name='Dealer1')
        self.tag = Tag.objects.create(name='Tag1')
        for i in range(5):
            car = Car.objects.create(title=f'Car{i}', description='Desc', price=5000+i, dealer=self.dealer)
            car.tags.add(self.tag)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('cars' in response.context)
        self.assertEqual(len(response.context['cars']), 3)

    def test_car_list_view(self):
        response = self.client.get(reverse('cars-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cars']), 5)
