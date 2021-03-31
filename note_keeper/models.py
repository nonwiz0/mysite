from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    content = models.TextField()
    doc = models.DateTimeField('date published', auto_now_add=True)
    modify_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return "Title: {}".format(self.title) 
