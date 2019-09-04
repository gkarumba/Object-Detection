from django.db import models
# from .models import File

# class File(models.Model):
#     file = models.FileField(blank=False, null=False)
#     def __str__(self):
#         return self.file.name

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    # remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)