from django.db import models

# Create your models here.
# This is a class that will become a database table afterward which currently inherits from 'models.Model'.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()

    def __str__(self):
        return self.title