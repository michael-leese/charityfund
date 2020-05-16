from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from accounts.models import User, UserProfile, Org
from django.contrib.auth.forms import UserCreationForm


#Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#User Profile Form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'profile_picture']

#User Registration Form
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True)
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return password2

#Organisation Registration Form
class OrgRegistrationForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = ['organisation', 'org_type', 'bio', 'image']

