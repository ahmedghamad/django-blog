from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import CollaborateRequest, About

# Create your tests here.

class TestAboutViews(TestCase):

    def setUp(self):
       """Creates about me content"""
       self.about = About(title="About me test",
                        content="This about me test content" )
       self.about.save()

    def test_about_render(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About me test", response.content)
        self.assertIn(b"This about me test content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)


def test_collaboration_rquest(self):
    post_data ={
        'name':'Ahmed',
        'email':'manchester-88@hotmail.com',
        'message': 'Lets collaborate'
    }
    response = self.client.post(reverse(
            'about'), post_data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content
        )