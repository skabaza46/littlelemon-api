from datetime import datetime
from django.test import TestCase
from django.utils.timezone import make_aware
from ..models import Booking, Menu


class MenuTest(TestCase):

    def test_get_item(self):

        item = Menu.objects.create(title="IceCream", price=5.80, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 5.8")

class BookingTest(TestCase):

    def test_get_booking(self):
        booking_date = make_aware(datetime.strptime("2023-01-17", "%Y-%m-%d"))

        booking = Booking.objects.create(name="Chris King", no_of_guests=4, booking_date=booking_date)

        self.assertEqual(booking.name, "Chris King")