from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import signup
from ..forms import SignUpForm

# Create your tests here.
class SignUpTests(TestCase):
	def test_signup_status_code(self):
		url = reverse('signup')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)
	#def test_signup_url_resolves_signup_view(self):
		#view = resolve('/signup/')
		#self.assertEquals(view.func, signup)