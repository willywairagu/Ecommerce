from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    full_names = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your full names"
        }
    ))
    Email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email address"
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Enter your message here:"
        }
    ))

    # def clean_Email(self):
    #     Email = self.cleaned_data.get("Email")
    #     if not "gmail.com" in Email:
    #         raise forms.ValidationError("Email not gmail.com")
    #     return Email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is Wrong.")





