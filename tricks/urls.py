from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^tricks/(?P<trick_slug>[\w|\W]+)/$', views.trick_detail)
]