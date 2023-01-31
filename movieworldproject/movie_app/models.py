from django.db import models

class Movieworld(models.Model):
    name=models.CharField(max_length=320)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name

