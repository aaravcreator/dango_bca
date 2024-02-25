from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255,null=True,)
    completed_status = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='todos',)
    photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now = True,null=True)
    def __str__(self):
        return f"{self.title}"

    