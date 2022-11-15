from django.test import TestCase
from countries.models import Country


class CountryTest(TestCase):
    def test_valid_country(self):
        self.assertEqual(2, 1)
