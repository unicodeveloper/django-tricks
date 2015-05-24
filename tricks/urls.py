from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^tricks/(?P<trick_slug>[\w|\W]+)/$', views.trick_detail),
    url(r'^user/tricks/new/$', views.trick_new, name='trick_new'),
    url(r'^user/tricks/(?P<trick_slug>[\w|\W]+)/edit/$', views.trick_edit, name='trick_edit')
]