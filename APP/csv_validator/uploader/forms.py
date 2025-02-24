from django import forms
from .models import CSVFile

# Create your views here.

class CSVUploadForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ['file']