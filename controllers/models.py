from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models


class ImageAttachment(models.Model):
    image = models.ImageField(upload_to="upload")

