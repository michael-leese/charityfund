from django.test import TestCase
from .models import User, UserProfile, Org
from django.utils import timezone

class TestModels(TestCase):
    #Test the userprofile model
    def test_create_userprofile(self):
        user = User.objects.create_user(id=1, username='testuser', password='Test123*')
        profile = UserProfile(user=user, nickname='testnickname', profile_picture='some_image.png')
        profile.save()
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.nickname, 'testnickname')
        self.assertEqual(profile.profile_picture, 'some_image.png')

    #Test Org Model
    def test_create_org(self):
        REG_CHARITY = 'Registered Charity'
        COM_PRO = 'Community Project'
        ORG_TYPE_CHOICES = (
            (REG_CHARITY, 'Registered Charity'),
            (COM_PRO, 'Community Project')
        )
        user = User.objects.create_user(id=1, username='testuser', password='Test123*')
        org = Org(user=user, organisation='testorg', org_type=COM_PRO, 
                  bio='test bio for org', image='some_org.png')
        org.save()
        self.assertEqual(org.user, user)
        self.assertEqual(org.organisation, 'testorg')
        self.assertEqual(org.org_type, 'Community Project')
        self.assertEqual(org.bio, 'test bio for org')
        self.assertEqual(org.image, 'some_org.png')

