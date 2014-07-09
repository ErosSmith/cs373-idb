import os
import sys
import unittest
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse


from django.test import TestCase
from wc_app.models import *


# class ModelTestCase(unittest.TestCase):


#     def test_country_model1(self):
        
#         country_test_dict1 = {'Brazil': ['BRA', 5]}
#         Country.objects.create(country_name="Brazil", country_code=country_test_dict1[0], rank = country_test_dict1[1])
#         Country_Brazil = Country.objects.get(country_name="Brazil")
        
#         self.assertEqual(Country_Brazil.country_name, "Brazil")
#         self.assertEqual(Country_Brazil.country_code, "BRA")
#         self.assertEqual(Country_Brazil.rank, 5)


# main()
