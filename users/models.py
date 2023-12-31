from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    email_verify = models.BooleanField(default=False)

    chat_id = models.CharField(max_length=10, verbose_name='чат',  **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
