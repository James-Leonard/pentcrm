from audioop import reverse
from urllib import response
from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):

    def test_status_code(self):
        #todo some sort of test
        response =  self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)

    #def test_template_name(self):
        #todo some sort of test
       # pass