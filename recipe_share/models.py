from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_pic = models.ImageField(default='default_food.jpg', upload_to='profile_pics')
    time_to_prep = models.TextField(max_length=100)
    recipe_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='recipes')

    def __str__(self):
        return self.recipe_name
    
    def get_absolute_url(self):
        return reverse('recipe_share-home')
    
    def total_likes(self):
        return self.likes.count()

    def save(self):
        super().save()

        img = Image.open(self.recipe_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.recipe_pic.path)

class Comment(models.Model):
    post = models.ForeignKey(Recipe, related_name='comments' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.body