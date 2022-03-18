from django.contrib import admin
from .models import Tag, Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author",)
    list_filter = ("author", "tags")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)