"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-secret-key")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", ["*"])
