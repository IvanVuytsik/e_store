from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory
        User.objects.create(username='admin')
        Category.objects.create(name='Shirts', slug='shirts')
        Product.objects.create(category_id=1, title='Marigold',
                     created_by_id=1, slug='marigold', price='55.00',
                     image='marigold')

    def test_url_allowed_hosts(self):
        """
        allowed clients
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        """
        response = self.c.get('/')  
        self.assertEqual(response.status_code, 200)          

    def test_product_detail_url(self):
        """
        product response
        """
        response = self.c.get(reverse('store:product_detail', args=['marigold']))
        self.assertEqual(response.status_code, 200)  

    def test_category_detail_url(self):
        """
        category response
        """
        response = self.c.get(reverse('store:category_list', args=['shirts']))
        self.assertEqual(response.status_code, 200) 

    def test_homepage_html(self):
        """
        html response test (store.views all_products)
        """
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        """ check html elements"""
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)


    def test_view_function(self):
        request = self.factory.get('/item/marigold')
        response = all_products(request)
        html = response.content.decode('utf8')
        """ check html elements"""
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)



# @skip('demonstate skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

