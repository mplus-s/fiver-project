from django.db import models
from cuser.models import AbstractCUser

# Create your models here.


class User(AbstractCUser):
    school = models.CharField(max_length=255, null=True)
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_messages(self):
        from messenger.models import Message
        messages = Message.get_user_messages(user_id=self.id)
        return messages
    
    def get_messages_for_product(self, product_uid):
        from messenger.models import Message
        messages = Message.get_user_messages_for_product(user_id=self.id, product_uid=product_uid)
        return messages


