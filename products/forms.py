from django import forms

class FileUploadForm(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    features = forms.CharField(max_length=500)

# from django import forms

# class MultipleImageField(forms.MultiValueField):
#     def __init__(self, *args, **kwargs):
#         fields = (
#             forms.ImageField(),
#         )
#         super().__init__(fields, *args, **kwargs)

#     def compress(self, data_list):
#         return data_list

# class ImageUploadForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     images = MultipleImageField()
