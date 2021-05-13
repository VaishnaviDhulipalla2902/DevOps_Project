from library.models import Post
from django.test import TestCase


""" class TestModels(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            title = 'Harry Potter',
            content = 'wizarding school',
        )

    def test_post_is_saved(self):
        self.assertEquals(self.post1.get_absolute_url(),1) """
class TestLibModels(TestCase):
    def test_model_str(self):
        title = Post.objects.create(title = "Harry Potter")
        content = Post.objects.create(content = "Wizarding School")
        self.assertEqual(str(title),"Harry Potter")