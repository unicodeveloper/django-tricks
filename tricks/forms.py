from django import forms
from .models import Trick

class TrickForm(forms.ModelForm):

    class Meta:
        model = Trick
        fields = ('title', 'description', 'code')
