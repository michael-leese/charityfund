from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from appeals.models import Appeal
from .widgets import BootstrapDateTimePickerInput

#Appeal Form
class AppealForm(forms.ModelForm):
    '''
    Appeals form with customised datepicker
    '''
    target_date = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=BootstrapDateTimePickerInput())

    class Meta:
        model = Appeal
        fields = ['title', 'bio', 'tags', 'target_date', 'money_target', 'latitude', 'longitude', 'image']
