from django.db import models
# from avina.storage import select_storage

class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="categories")

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.__repr__()}"
    