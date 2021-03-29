from django.db import models
from django.utils import timezone
import datetime

class Note(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    content = models.TextField()
    now = timezone.now()
    doc = models.DateTimeField('date published', default=now)
    modify_date = models.DateTimeField('date published', default=now)

    def __str__(self):
        return "Title: {} \nContent: {} \nDate of Creation: {} \nLast modify: {}".format(self.title, self.content, self.doc, self.modify_date) 
