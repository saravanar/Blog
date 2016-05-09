from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import BlogManaging

urlpatterns = [
    url(r'^$', csrf_exempt(BlogManaging.as_view())),
]