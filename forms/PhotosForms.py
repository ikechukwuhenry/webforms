from django import forms

class PhotosForms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField(max_length=128, label="Please enter the title of the page.")
    url = forms.URLField(max_length=200, initial="Please enter the URL of the page.")
