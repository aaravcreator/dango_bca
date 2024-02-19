from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255,null=True,)
    completed_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    