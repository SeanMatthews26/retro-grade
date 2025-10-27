from django.contrib import admin
from .models import Game, Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)