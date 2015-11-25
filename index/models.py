from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return self.username
