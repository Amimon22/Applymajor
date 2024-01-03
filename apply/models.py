from django.db import models

# Create your models here.
class Source(models.Model):
    src_file = models.CharField(max_length=225, default='')
    src_name = models.CharField(max_length=225, default='')
    src_link = models.CharField(max_length=225, default='')
    result_text = models.CharField(max_length=4096, default='')
    status = models.CharField(max_length=10, default='')
    usage_flag = models.CharField(max_length=10, default='')
    create_at = models.DateTimeField()