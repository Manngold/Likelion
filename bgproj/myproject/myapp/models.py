from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pubDay = models.DateTimeField('date pubulished')

    def __str__(self):
        return self.title