from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    doc = models.DateTimeField('date published')
    modify_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return "ID: {} \nTitle: {} \nContent: {} \nDate of Creation: {} \nLast modify: {}".format(self.id, self.title, self.content, self.doc, self.modify_date) 
# class Notebook(models.Model):
#     note = models.ForeignKey(Note, on_delete=models.CASCADE)
#     modify_date = models.DateTimeField('date modified')

#     def __str__(self):
#         return "Note: {} \nModify_date: {}".format(self.note, self.modify_date)
     