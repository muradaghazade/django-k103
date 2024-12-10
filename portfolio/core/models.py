from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description  = models.TextField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'



# class Author(models.Model):
