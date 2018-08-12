#-------------------------------------------------#
# Title: feeds.py
# Dev:   Scott Luse
# Changelog:
# Aug 12, 2018: RSS feed
#-------------------------------------------------#

from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post


class LatestPostsFeed(Feed):
   title = "Blog Posts"
   link = "/feeds/"
   description = "Posts published in my blog."

   def items(self):
       return Post.objects.order_by('-published_date')[:5]

   def item_title(self, item):
       return item.title

   def item_description(self, item):
       return item.text

   def item_link(self, item):
       return reverse('blog_detail', args=[item.pk])
