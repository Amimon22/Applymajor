from django.db import models

# Create your models here.
class Startpage(models.Model):
    def __str__(self):
        return self.name