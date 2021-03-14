from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    doc = models.DateTimeField('date published')

    def __str__(self):
        return "ID: {} \nTitle: {} \nContent: {} \nDate of Creation: {}".format(self.id, self.title, self.content, self.doc)
 
  