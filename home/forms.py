from django import forms


class ContactUsForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=150, required=False)
    message = forms.CharField(label='message', widget=forms.Textarea, required=False)

