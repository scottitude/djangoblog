from django.urls import path
from .views import list_view, detail_view

from django.conf.urls import url, include
from rest_framework import routers
from myblog import views
from myblog.feeds import LatestPostsFeed

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^feeds/$', LatestPostsFeed(), name='feeds'),
]
