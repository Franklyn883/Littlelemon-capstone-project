from django.test import TestCase
from .models import Menu, Booking

# Create your tests here.

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream",price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
