from django.contrib import admin
from .models import Game, Review, Comment

# Register your models here.
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Comment)