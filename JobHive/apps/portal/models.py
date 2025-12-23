from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    ROLE_CHOICES = (
        ("admin", "Admin"),  # use only onetime
        ("user", "User"),
        ("company", "Company"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")

    # Login with email instead of username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} ({self.role})"
        # return self.username
