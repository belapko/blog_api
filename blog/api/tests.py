from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Post, Category
from rest_framework.authtoken.models import Token
from django.urls import reverse


class PostTests(APITestCase):
    def setUp(self) -> None:
        user_test1 = User.objects.create_user(username='test1', password='test1')
        user_test1.save()

        user_test2 = User.objects.create_user(username='test2', password='test2')
        user_test2.save()

        post1 = Post.objects.create(title='testPost', body='testPost', owner=user_test1)
        category1 = Category.objects.create(name='Cats', owner=user_test1)

    def test_get_posts(self):
        # self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token1.key)
        response = self.client.get('http://127.0.0.1:8000/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_posts(self):
        self.client.login(username='test1', password='test1')
        data = {
            'title': 'test',
            'body': 'test',
        }
        response = self.client.post('http://127.0.0.1:8000/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_posts_authorized(self):
        put_data = {
            'body': 'new body',
            'categories': 1,
        }
        self.client.login(username='test1', password='test1')
        response = self.client.put('http://127.0.0.1:8000/posts/1/', data=put_data)
        response_data = self.client.get('http://127.0.0.1:8000/posts/1/').data
        self.assertEqual(response_data['body'], put_data['body'])
        self.assertEqual(response_data['categories'][0], put_data['categories'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_posts_unauthorized(self):
        put_data = {
            'body': 'new body fail',
        }
        response = self.client.put('http://127.0.0.1:8000/posts/1/', data=put_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
