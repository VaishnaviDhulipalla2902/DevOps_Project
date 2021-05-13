from library.models import Post
from users.models import Profile
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
import time

class TestPostListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_post_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        #time.sleep(20)