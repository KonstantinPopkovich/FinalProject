from django.test import TestCase
from rest_framework import serializers
from bookshop.models import Authors, Category, Books
from .serializers import BooksSerializer

class BooksSerializerTestCase(TestCase):
    def setUp(self):
        self.author = Authors.objects.create(name_authors='TestAuthor')
        self.category = Category.objects.create(name_category='TestCategory')
        self.book_data = {
            'writer': self.author.id,
            'category': self.category.id,
            'name': 'asd',
            'annotation': 'asdd',
            'rating': '4.5',
            'price': '29.99',
            'amount': 100,
        }
        self.serializer = BooksSerializer(data=self.book_data)

    def test_serializer_data_valid(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data, self.book_data)

    def test_serializer_data_invalid(self):
        self.book_data['name'] = ''
        self.serializer = BooksSerializer(data=self.book_data)
        self.assertFalse(self.serializer.is_valid())
        self.assertIn('name', self.serializer.errors)

    def test_serializer_save(self):
        self.assertTrue(self.serializer.is_valid())
        book = self.serializer.save()
        self.assertEqual(book.name, 'asd')
        self.assertEqual(book.writer, self.author)
        self.assertEqual(book.category, self.category)

    def test_serializer_update(self):
        self.assertTrue(self.serializer.is_valid())
        book = self.serializer.save()
        self.book_data['name'] = 'asddd'
        self.serializer = BooksSerializer(book, data=self.book_data)
        self.assertTrue(self.serializer.is_valid())
        self.serializer.save()
        updated_book = Books.objects.get(id=book.id)
        self.assertEqual(updated_book.name, 'asddd')

    def tearDown(self):
        Authors.objects.all().delete()
        Category.objects.all().delete()
        Books.objects.all().delete()
