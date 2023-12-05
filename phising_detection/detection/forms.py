from django import forms

class dataForm(forms.Form):
    EmailData = forms.CharField(widget=forms.Textarea(attrs={'rows':8}))