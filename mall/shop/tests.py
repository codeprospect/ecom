from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductModelTests(TestCase):

    def product_was_created_successfully(self):
        new_product = Product()
