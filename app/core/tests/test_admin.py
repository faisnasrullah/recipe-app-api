from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model.Object.create_superuser(
            email = 'admin@ampasdev.id',
            password = '12345678'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model.Object.create_user(
            email = 'user@ampasdev.id',
            password = '12345678',
            name = 'User 01'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)