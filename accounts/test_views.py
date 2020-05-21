from django.test import TestCase
from .models import User, UserProfile, Org
from .forms import OrgRegistrationForm
from django.contrib import auth
from django.shortcuts import get_object_or_404

class TestViews(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser', password='Test123*')  
        test_user1_profile = UserProfile.objects.create(user=test_user1, nickname='testnickname')  
        test_user1.save()
        test_user1_profile.save()
        test_org = Org(user=test_user1 ,organisation="test",bio="initial")
        test_org.save()

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_about_page(self):
        page = self.client.get("/accounts/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_org_registration_page(self):
        login = self.client.login(username='testuser', password='Test123*')
        page = self.client.get("/accounts/register_org/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "organisation.html")

    def test_edit_org_page(self):
        login = self.client.login(username='testuser', password='Test123*')
        test_user1 = User.objects.get(username='testuser')
        org = Org.objects.get(user=test_user1)
        form = OrgRegistrationForm(instance=org)
        page = self.client.get("/accounts/edit_org/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "editorg.html")

    def test_edit_org(self):
        login = self.client.login(username='testuser', password='Test123*')
        test_user1 = User.objects.get(username='testuser')
        org = Org(user=test_user1 ,organisation="test",bio="changed")
        org.save()
        self.assertEqual(org.bio, "changed")

    def test_edit_userprofile(self):
        login = self.client.login(username='testuser', password='Test123*')
        user = User.objects.get(username='testuser')
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.nickname, "testnickname")
        profile = UserProfile(nickname="changednickname")
        profile.save()
        self.assertEqual(profile.nickname, "changednickname")

    def test_user_authenticated(self):
        login = self.client.login(username='testuser', password='Test123*')
        test_user1 = User.objects.get(username='testuser')
        authorised_user = False
        if test_user1.is_authenticated:
            authorised_user = True
        self.assertTrue(authorised_user)

    def test_has_org(self):
        login = self.client.login(username='testuser', password='Test123*')
        test_user1 = User.objects.get(username='testuser')
        org = Org.objects.filter(user=test_user1)
        if org:
            hasOrg = True
        else:
            hasOrg = False
        self.assertTrue(hasOrg)
    
    def test_edit_org_where_doesnt_exist(self):
        page = self.client.get("/accounts/edit_org/2")
        self.assertEqual(page.status_code, 404)

