

from django import forms
from .models import Dc, DcCover, Dcinfo


class DcForm(forms.ModelForm):
    class Meta:
        
        
        model = Dc
        
        fields = ('title', 'villains')



class DcCoverForm(forms.ModelForm):
    class Meta:
        model = DcCover
        exclude = ('dc',) 
        fields = ('image',)

class DcinfoForm(forms.ModelForm):
    class Meta:
        model = Dcinfo
        exclude = ('dc',)
        fields = ('title', 'track')