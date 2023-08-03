from django.test import TestCase
from .models import Menu, Booking

# Create your tests here.

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream",price=80, inventory=100)
        self.assertEqual(item.title, 'IceCream')
        self.assertEqual(item.price, 80)
        
class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="John",no_of_guest=5, booking_date="2023-08-03")
        self.assertEqual(item.name, 'John')
        self.assertEqual(item.no_of_guest, 5)