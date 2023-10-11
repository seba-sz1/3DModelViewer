from django.db import models


class ThreeDModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    filePath = models.FilePathField(max_length=1000)

    def __str__(self):
        return self.name
