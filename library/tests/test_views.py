from django.http import HttpResponse
from django.test import TestCase, Client, client
from django.urls import reverse
from library.models import Post
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.library_url = reverse('library-home')
        self.detail_url = reverse('post-detail',args=[9])
        """ self.post1 = Post.objects.create(
        title='Harry Potter',
        content = 'wizard school',
        ) """
    
    def test_post_list_GET(self):
        response = self.client.get(self.library_url)
        self.assertEquals(HttpResponse.status_code, 200)
        self.assertTemplateUsed(response,'library/home.html')
    
    """ def test_post_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(HttpResponse.status_code, 200)
        self.assertTemplateUsed(response,'library/user_posts.html') """