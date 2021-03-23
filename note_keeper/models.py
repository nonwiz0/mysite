from django.db import models
from django.utils import timezone
import datetime

class Note(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    content = models.TextField()
    doc = models.DateTimeField('date published', default=timezone.now())
    modify_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return "ID: {} \nTitle: {} \nContent: {} \nDate of Creation: {} \nLast modify: {}".format(self.id, self.title, self.content, self.doc, self.modify_date) 
