from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Hamza',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_invalid(self):
        form = CollaborateForm({'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'})
        self.assertFalse(form.is_valid(), msg='Name is missing')
    
    def test_email_is_invalid(self):
        form = CollaborateForm({ 'name': 'Matt',
            'email': '',
            'message': 'Hello!'})
        self.assertFalse(form.is_valid(), msg='Email is missing')

    def test_message_is_invalid(self):
        form = CollaborateForm({'name': 'Matt',
            'email': 'test@test.com',
            'message': ''})
        self.assertFalse(form.is_valid(), msg='Message is missing')