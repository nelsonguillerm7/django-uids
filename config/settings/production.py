"""Production settings."""

from .base import *  # NOQA
from .base import env

# Base
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", ["*"])
