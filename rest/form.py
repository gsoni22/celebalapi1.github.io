from django import forms
from .models import imageModel
class imageFORM(forms.ModelForm):
    class Meta:
        model = imageModel
        exclude = []
        widgets = {
            'image1': forms.FileInput(attrs={'class': 'form-horizontal'}),
            'image2': forms.FileInput(attrs={'class': 'form-horizontal'}),
            'image3': forms.FileInput(attrs={'class': 'form-horizontal'}),
            'image4': forms.FileInput(attrs={'class': 'form-horizontal'}),
        }

class FileFieldForm(forms.Form):
    file_field = forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'multiple': True}))