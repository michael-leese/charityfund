from django import forms
from payments.models import Order


class MakePaymentForm(forms.Form):
    """
    Creates a form to capture the payment details of the card being used
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(20, 36)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
    Create an order form to store the donation informatioin and details of the donor
    """
    class Meta:
        model = Order
        fields = (
            'full_name', 'street_address1', 'street_address2', 
            'town_or_city', 'country', 'postcode', 'comment', 
            'anonymous', 'amount'
        )
