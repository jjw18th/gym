from django.db import models

class message(models.Model):
    name=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)
    def __str__(self):
     return self.name;
