from django.test import TestCase
from .models import User, UserProfile, Org
from .forms import OrgRegistrationForm

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