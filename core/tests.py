from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import JobListing

class JobListingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.job_listing = JobListing.objects.create(title='Test Job', description='Test Description')

    def test_create_job_listing(self):
        response = self.client.post('/job-listings/', {'title': 'New Job', 'description': 'New Description'})
        self.assertEqual(response.status_code, 201)

    def test_get_job_listings(self):
        response = self.client.get('/job-listings/')
        self.assertEqual(response.status_code, 200)