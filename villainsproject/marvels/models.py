
import re
from django.contrib.auth import get_user_model
from django.db import models

from villains.models import Villain






class Marvel(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='marvels')
    
    villains = models.ManyToManyField(Villain, blank=True, related_name='marvels')
    
    
    
    

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    
    
    def __str__(self):
        return self.title[:50]









class MarvelCover(models.Model):
    marvel = models.OneToOneField(Marvel, on_delete=models.CASCADE, primary_key=True, related_name='marvelcover')
    image = models.ImageField(upload_to='marvels/marvelcovers/%Y/%m/%d/')

    
    
    
    
    

    def __str__(self):
        return self.image






class Marvelinfo(models.Model):
    album = models.ForeignKey(Marvel, on_delete=models.CASCADE, related_name='marvelinfo')
    title = models.CharField(max_length=255)
    
    
    track = models.FileField(upload_to='marvels/marvelinfo/%Y/%m/%d/')

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    def __str__(self):
        return self.title[:50]