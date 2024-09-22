from django.db import models
from helpers.models  import TrackingModel
from authentication.models import User


class Todo(TrackingModel):

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str :
        ordering = ['created_at']
        return self.title