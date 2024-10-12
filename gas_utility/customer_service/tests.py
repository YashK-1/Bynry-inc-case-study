from django.test import TestCase
from django.contrib.auth.models import User
from .models import ServiceRequest

class ServiceRequestTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.request = ServiceRequest.objects.create(
            customer=self.user, request_type='Maintenance', description='Fix gas leak'
        )

    def test_request_creation(self):
        self.assertEqual(self.request.request_type, 'Maintenance')
