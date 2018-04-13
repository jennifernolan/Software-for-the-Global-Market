from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User

from .views import cities

# Create your tests here.
class CititesTests(TestCase):
	def setUp(self):
		User.objects.create_user(username='john', email='john@doe.com', password='123')
		
		url = reverse('cities')
		self.response = self.client.get(url)
	
	def test_home_view_status_code(self):
		url = reverse('cities')
		reponse = self.client.get(url)
		self.assertEquals(self.response.status_code, 404)