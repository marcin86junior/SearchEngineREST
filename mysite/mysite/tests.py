from django.test import TestCase
from getxml.models import Package


class ModelsTestCase(TestCase):

    def test_Package_model(self):
        """Package model work properly"""
        package = Package.objects.create(
            author='Test author',
            title="Test title",
            link="Test link",
            guid="Test guid",
            description="Test description",
            pubDate="2022",
        )
        self.assertEqual(package.title, 'Test title')

class ViewsTestCase(TestCase):
    fixtures = ['datafix.json']

    def test_bad_link(self):
        resp = self.client.get('http://127.0.0.1:8000/abc/')
        self.assertEqual(resp.status_code, 404)

    def test_main_page(self):
        """The main page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')

    def test_package_page(self):
        """The search page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/package/?search=')
        self.assertEqual(response.status_code, 200)

    def test_admin_link_turned_off(self):
        """The admin should be turned-off"""
        resp = self.client.get('http://127.0.0.1:8000/admin/')
        self.assertEqual(resp.status_code, 404)

    def test_options_site(self):
        response = self.client.get('/options/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Options')

    def test_addpackage_site(self):
        response = self.client.get('/options/addpackage/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data is added.')

    def test_addbooks1_site(self):
        response = self.client.get('/options/addbooks1/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data is added.')

    def test_addbooks2_site(self):
        response = self.client.get('/options/addbooks2/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data is added.')

    def test_deletepackages_site(self):
        response = self.client.get('/options/deletepackages/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data is deleted.')

    def test_options_json_site(self): 
        response = self.client.get('/options/json/') 
        self.assertEqual(response.status_code, 200) 

    def test_options_uploads_site(self):
        response = self.client.get('/options/basic-upload/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Read file') 
        
    def test_searchHTML_site(self):
        response = self.client.get('/searchHTML/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search results')
    

'''
# REST tests

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ReadUserTest(APITestCase):
    def setUp(self):
        self.package = Package.objects.create(author='Test author', title="Test title")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('package/'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('package-detail', args=[self.package.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
'''

'''
Test that should be done:
- searching data with fixtures...
- restAPI - search / APIfactories...
'''