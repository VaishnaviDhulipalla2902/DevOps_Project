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