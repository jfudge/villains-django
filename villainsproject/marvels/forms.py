

from django import forms
from .models import Marvel, MarvelCover, Marvelinfo


class MarvelForm(forms.ModelForm):
    class Meta:
        
        
        model = Marvel
        
        fields = ('title', 'villains')



class MarvelCoverForm(forms.ModelForm):
    class Meta:
        model = MarvelCover
        exclude = ('marvel',) 
        fields = ('image',)

class MarvelinfoForm(forms.ModelForm):
    class Meta:
        model = Marvelinfo
        exclude = ('marvel',)
        fields = ('title', 'track')