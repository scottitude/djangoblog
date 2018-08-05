#-------------------------------------------------#
# Title: admin.py
# Dev:   Scott Luse
# Date:  Aug 04, 2018
# Change so that you can only add categories to posts
#-------------------------------------------------#

from django.contrib import admin

from myblog.models import Post
from myblog.models import Category

# admin.site.register(Post)
# admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

admin.site.register(Post, PostAdmin)

