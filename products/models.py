from django.db import models
# from avina.storage import select_storage
from avina.settings import AUTH_USER_MODEL
from django.db.models.deletion import CASCADE, RESTRICT
from uuid import uuid4
from django.contrib.auth import get_user_model


def generate_uid():
    return uuid4().hex

class CartItemStatus:
    PENDING = "Pending"
    SOLD = "Sold"
    CANCELLED = "Cancelled"

    @staticmethod
    def choices():
        return (
            (CartItemStatus.PENDING, CartItemStatus.PENDING),
            (CartItemStatus.SOLD, CartItemStatus.SOLD),
            (CartItemStatus.CANCELLED, CartItemStatus.CANCELLED),
        )

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0   )    
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

class CartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(choices=CartItemStatus.choices(), max_length=20, default=CartItemStatus.PENDING)
    seller_confirmation = models.BooleanField(default=False)
    buyer_confirmation = models.BooleanField(default=False)

    def make_sold(self):
        self.status = CartItemStatus.SOLD

    def cancel(self):
        self.status = CartItemStatus.CANCELLED

    @property
    def seller(self):
        return self.product.added_by
