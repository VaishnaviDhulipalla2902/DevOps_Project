from django.test import TestCase, SimpleTestCase
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

class TestForms(TestCase):
    def test_create_form_with_data(self):
        form = UserRegisterForm(data={
            'username':'qwerty',
            'email':'qwerty123@xyz.com',
            'password1':'abcd1234',
            'password2':'abcd1234'})

        self.assertFalse(form.is_valid()) #should be assertTrue not False

    def test_create_form_no_data(self):
        form = UserRegisterForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)