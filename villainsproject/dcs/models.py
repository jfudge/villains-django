
import re
from django.contrib.auth import get_user_model
from django.db import models

from villains.models import Villain






class Dc(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='dcs')
    
    villains = models.ManyToManyField(Villain, blank=True, related_name='dcs')
    
    
    
    

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    
    
    def __str__(self):
        return self.title[:50]









class DcCover(models.Model):
    dc = models.OneToOneField(Dc, on_delete=models.CASCADE, primary_key=True, related_name='dccover')
    image = models.ImageField(upload_to='dcs/dccovers/%Y/%m/%d/')

    
    
    
    
    

    def __str__(self):
        return self.image






class Dcinfo(models.Model):
    dc = models.ForeignKey(Dc, on_delete=models.CASCADE, related_name='dcinfo')
    title = models.CharField(max_length=255)
    
    
    track = models.FileField(upload_to='dcs/dcinfo/%Y/%m/%d/')

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    def __str__(self):
        return self.title[:50]