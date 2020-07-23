from django import forms
from .models import BillingProfile

# class PaymentSelectForm(forms.Form):
#     Mpesa_number = forms.CharField(widget=forms.TextInput(
#         attrs={
#             "class": "form-control",
#             "placeholder": "eg 2547........"
#         }
#     ))


# to add placeholder functionality to show format
class PaymentSelectForm(forms.ModelForm):
    class Meta:
        model = BillingProfile
        fields = [
            'Mpesa_number'
        ]