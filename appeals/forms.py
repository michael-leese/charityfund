from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from appeals.models import Appeal
from tempus_dominus.widgets import DatePicker

#Appeal Form
class AppealForm(forms.ModelForm):
    '''
    Appeals form with customised datepicker
    '''
    target_date = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=DatePicker(options={
                                                                                        'format': 'DD/MM/YYYY',
                                                                                    },
                                                                                    attrs={
                                                                                        'append': 'fa fa-calendar',
                                                                                        'icon_toggle': True,
                                                                                    }))

    class Meta:
        model = Appeal
        fields = ['title', 'bio', 'tags', 'target_date', 'money_target', 'latitude', 'longitude', 'image']
