import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from wiki.models import Page
from django.urls import reverse

class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """Tests the slug generated when saving the page"""
        #Create a user for this test
        user = User()
        user.save()

        #Create and save page to DB
        page = Page(title="My Test Page", content="test", author=user)
        page.save()
        self.assertEqual(page.slug, 'my-test-page')

class PageListViewTests(TestCase):

    def test_multiple_pages(self):
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test", author=user)

        #Make GET request
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

class PageDetailViewTests(TestCase):

    def test_page_loads_for_specific_page(self, *args):
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)

        response = self.client.get('/my-test-page/')

        self.assertEqual(response.status_code, 200)

class PageCreateView(TestCase):

    
