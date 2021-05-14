from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from library.views import about, PostListView, PostCreateView, PostDetailView, UserPostListView, PostDeleteView, PostUpdateView, buy, borrow

class TestUrls(SimpleTestCase):
    def test_library_home_url_resolves(self):
        url = reverse('library-home')
        self.assertEquals(resolve(url).func.view_class,PostListView)

    def test_post_url_resolves(self):
        url = reverse('user-posts', args=['some_post'])
        self.assertEquals(resolve(url).func.view_class,UserPostListView)

    def test_post_detail_url_resolves(self):
        url = reverse('post-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class,PostDetailView)

    def test_post_create_url_resolves(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class,PostCreateView)

    def test_post_update_url_resolves(self):
        url = reverse('post-update',args=[1])
        self.assertEquals(resolve(url).func.view_class,PostUpdateView)

    def test_post_delete_url_resolves(self):
        url = reverse('post-delete',args=[1])
        self.assertEquals(resolve(url).func.view_class,PostDeleteView)

    def test_library_about_resolves(self):
        url = reverse('library-about')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,about)

    def test_buy_book(self):
        url = reverse('buy-book')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,buy)

    def test_buy_borrow(self):
        url = reverse('buy-borrow')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,borrow)