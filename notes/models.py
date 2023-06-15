from django.db import models
from users.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shared_with = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'notes'