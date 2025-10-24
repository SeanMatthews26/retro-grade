from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    platform = models.CharField(max_length=200)
    release_year = models.IntegerField()
    developer = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()


class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0,
    )


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
