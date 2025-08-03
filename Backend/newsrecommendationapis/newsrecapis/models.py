from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    preferred_news_categories = models.JSONField(blank=True, default=list)

    # Add related_name to avoid reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='newsrecapis_user_set',  # Use a unique name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='newsrecapis_user_set',  # Use a unique name
        blank=True
    )

    def __str__(self):
        return self.username
