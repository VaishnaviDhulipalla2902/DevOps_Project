from users.models import Profile
from django.test import TestCase
from django.contrib.auth.models import User

class TestUserModels(TestCase):
    def test_model_user(self):
        testuser = User.objects.create_user(username = 'testuser', password = '12345')
        testuser2 = User.objects.create_user(username = 'testuser2', password = '12345')
        title = Profile.objects.create()
        title.user.set([testuser.pk,testuser2.pk])
        self.assertEqual(title.user.count(),2)