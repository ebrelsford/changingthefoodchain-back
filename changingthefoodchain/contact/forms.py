from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=200, required=False)
    text = forms.CharField(widget=forms.Textarea)
