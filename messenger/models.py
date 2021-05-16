from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.postgres.fields import ArrayField
# Create your models here.``

class Message(models.Model):
    product = models.ForeignKey("products.Product", on_delete=SET_NULL, related_name="messages", null=True)
    messages = ArrayField(models.JSONField())
    parties = ArrayField(models.IntegerField(), size=2)

    @classmethod
    def get_user_messages(cls, user_id):
        msgs  = cls.objects.filter(parties__contains=[user_id,]).all()
        return msgs
    
    @classmethod
    def get_user_messages_for_product(cls, user_id, product_uid):
        msgs = cls.objects.filter(parties__contains=[user_id,], product__uid=product_uid).first()
        return msgs

    def __repr__(self):
        return "product:\t{}\nmessages:\t{}\nparties:\t{}".format(self.product, self.messages, self.parties)