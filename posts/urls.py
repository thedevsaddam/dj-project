from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', 'posts.views.posts_home', name='home'),
]
