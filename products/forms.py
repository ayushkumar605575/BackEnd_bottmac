from django import forms

class FileUploadForm(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    features = forms.CharField(max_length=500)
