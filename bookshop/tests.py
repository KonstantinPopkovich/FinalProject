from django.test import TestCase
from .models import OfficeSupplies

class OfficeSuppliesModelTests(TestCase):
    def setUp(self):
        OfficeSupplies.objects.create(
            brand="Brand_Test",
            country_manufacturer="Country_Test",
            article_number=123,
            amount=50,
            rating=4.5,
            price=19.99
        )

    def test_office_supplies_creation(self):
        office_supplies = OfficeSupplies.objects.get(brand="Brand_Test")
        self.assertEqual(office_supplies.country_manufacturer, "Country_Test")
        self.assertEqual(office_supplies.article_number, 123)
        self.assertEqual(office_supplies.amount, 50)
        self.assertEqual(office_supplies.rating, 4.5)
        self.assertEqual(office_supplies.price, 19.99)

    def test_office_supplies_str_method(self):
        office_supplies = OfficeSupplies.objects.get(brand="Brand_Test")
        self.assertEqual(str(office_supplies), "Brand_Test")