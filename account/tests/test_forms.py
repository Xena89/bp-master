from account.forms import LoginForm, SettingsForm
from django.test import TestCase
from ticket.models import Ticket


class TicketFormTest(TestCase):
    fixtures = ['fixtures/accounts.json']

    def test_valid_login_form(self):
        data = {'username': "test_user2", 'password': "Coolpass123",}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_login_form(self):
        data = {'username': "test_user2", 'password': "fdsgsdfgfdg"}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_settings_form(self):
        data = {'sending_email_once_a_day': "True", }
        form = SettingsForm(data=data)
        self.assertTrue(form.is_valid())
