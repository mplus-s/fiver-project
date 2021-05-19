from django.db.models.fields import related
from avina.settings import AUTH_USER_MODEL
from users.models import User
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.postgres.fields import ArrayField

# Create your models here.``
class Message(models.Model):
    product = models.ForeignKey("products.Product", on_delete=SET_NULL, related_name="product", null=True)
    seller = models.ForeignKey(AUTH_USER_MODEL,on_delete=CASCADE, related_name="seller", null=False)
    buyer = models.ForeignKey(User,on_delete=CASCADE,null=False,related_name="buyer")
    datetime_sent = models.DateTimeField( auto_now_add=True)
    message = models.CharField( max_length=500)

    class Meta:
        ordering = ('datetime_sent',)
