from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME", None),
        'USER': os.environ.get("DB_USER", None),
        'PASSWORD':os.environ.get("DB_PASSWORD", None),
        'HOST': os.environ.get("DB_HOST", None),
        'PORT': os.environ.get("DB_PORT", 5432),
    }
}

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'

SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = os.environ["SENDGRID_EMAIL_SENDER"]

AWS_ACCESS_KEY_ID =os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY =os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME =os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'avina.storage.RemoteFileStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

DEFAULT_FILE_STORAGE = 'avina.storage.RemoteFileStorage'
