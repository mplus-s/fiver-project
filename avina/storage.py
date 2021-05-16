from django.core.files.storage import Storage, FileSystemStorage
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class LocalFileStorage(FileSystemStorage):
    pass

class RemoteFileStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    default_acl = 'public-read'


# def select_storage(location=""):
#     location = "uploads/"+location
#     return LocalFileStorage(location=location) if settings.DEBUG else RemoteFileStorage()

