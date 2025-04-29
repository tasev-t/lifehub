from django.contrib.auth.models import AbstractUser
from django.db import models

class FamilyGroup(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(AbstractUser):
    MODE_CHOICES = (
        ('personal', 'Personal'),
        ('family', 'Family'),
    )

    profile_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='personal')
    family_group = models.ForeignKey(
        FamilyGroup, related_name='members', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.username
