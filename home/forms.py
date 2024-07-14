from django import forms

from home.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ("subject", "message")
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Subject",
                "style": "width: 900px; ",
        }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Message",
        })
    }

