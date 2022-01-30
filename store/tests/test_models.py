from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Shirt', slug='shirt')

    def test_category_model_entry(self):
        """
        test Category model data insertion/types/field
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        test Category return name
        """
        data = self.data1
        self.assertEqual(str(data), 'Shirt')


#--------------------------------------------------------------

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Shirts', slug='shirts') #to build a product, category is required
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Marigold',
                     created_by_id=1, slug='marigold', price='55.00',
                     image='marigold')  #_id = added in the DB in the backend
 
    def test_products_model_entry(self):
        """
        test Product model data insertion/types/field
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Marigold') #returns string .models