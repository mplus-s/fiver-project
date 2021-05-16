from django.db import models
# from avina.storage import select_storage
from avina.settings import AUTH_USER_MODEL
from django.db.models.deletion import CASCADE, RESTRICT
from uuid import uuid4


def generate_uid():
    return uuid4().hex


class Product(models.Model):
    uid = models.CharField(default=generate_uid, unique=True, max_length=255)
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(
        "categories.Category", on_delete=RESTRICT, related_name="products")
    photo1 = models.ImageField(upload_to="products")
    photo2 = models.ImageField(upload_to="products")
    photo3 = models.ImageField(upload_to="products")
    photo4 = models.ImageField(upload_to="products")
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=RESTRICT, related_name="products")
    sold = models.BooleanField(default=False)

    def __repr__(self):
        return "Product:\t{}\nDescription:\t{}\nStatus:\t{}".format(self.name, self.description, self.status)
