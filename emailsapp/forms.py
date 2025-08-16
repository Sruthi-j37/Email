from django import forms
from emailsapp.models import Detail
class Detail(forms.ModelForm):
    class Meta:
        model=Detail
        fields='__all__'