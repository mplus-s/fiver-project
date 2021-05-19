from django.db import models
from cuser.models import AbstractCUser

# Create your models here.


class User(AbstractCUser):
    school = models.CharField(max_length=255, null=True)
    REQUIRED_FIELDS = ["first_name", "last_name"]




