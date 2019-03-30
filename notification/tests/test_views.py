from django.test import TestCase
from django.urls import reverse
from django.test.client import Client


class NotificationViewsTest(TestCase):
    fixtures = ['fixtures/accounts.json', 'fixtures/notification.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='master',password='Coollol888')

    def test_send_email_view(self, username='test_user', email='mail@test.ru', password='Testing1234'):
        url = reverse('send_email')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('success', str(resp.content))

    def test_one_a_day_view(self):
        url = reverse('one_a_day')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('success', str(resp.content))
