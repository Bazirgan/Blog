from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.author.username


