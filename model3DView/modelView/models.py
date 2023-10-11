from django.db import models


class ThreeDModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='files/')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.name} | {self.description}"
