from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Categories"
    
class Tag(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    featured_image = models.ImageField(upload_to="blog_featured_image/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
'''

Category
 - title

Tag 
Blog
- title
- category(FK -> Category)
- tags (MANY TO MANY)
- content 
- created_by (FK -> User)
- created_at 
- updated_at 
- published > boolean
'''