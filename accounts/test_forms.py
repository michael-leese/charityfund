from django.test import TestCase
from .forms import UserLoginForm, UserCreationForm, UserProfileForm, OrgRegistrationForm

class TestAccountForms(TestCase):
    
    def test_login_form(self):
        form = UserLoginForm({'username': 'testuser',
                              'password': 'Test123*'})
        self.assertTrue(form.is_valid())

    def test_login_form_no_password(self):
        form = UserLoginForm({'username': 'testuser',
                              'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
    
    def test_user_creation_form(self):
        form = UserCreationForm({'username': 'testuser',
                                 'first_name': 'tester',
                                 'last_name': 'check',
                                 'email': 'test@test.org',
                                 'password1': 'Test123*',
                                 'password2': 'Test123*'})
        self.assertTrue(form.is_valid())

    def test_user_creation_form_with_mismatch_password(self):
        form = UserCreationForm({'username': 'testuser',
                                 'first_name': 'tester',
                                 'last_name': 'check',
                                 'email': 'test@test.org',
                                 'password1': 'Test123*',
                                 'password2': 'Test123'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'The two password fields didn’t match.'])

    def test_user_profile_form_without_profile_picture(self):
        form = UserProfileForm({'nickname': 'testuser',
                                'profile_picture': '',
                                })
        self.assertTrue(form.is_valid())
    
    def test_user_profile_form_without_nickname(self):
        form = UserProfileForm({'nickname': '',
                                'profile_picture': '',
                                })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nickname'], [u'This field is required.'])

    def test_organisation_form_without_data(self):
        form = OrgRegistrationForm({'organisation': '',
                                    'org_type': '',
                                    'bio': '',
                                    'image': '',
                                    })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['organisation'], [u'This field is required.'])

    def test_organisation_form_without_image(self):
        form = OrgRegistrationForm({'organisation': 'testorg',
                                    'org_type': 'Registered Charity',
                                    'bio': 'Test bio',
                                    'image': '',
                                    })
        self.assertTrue(form.is_valid())