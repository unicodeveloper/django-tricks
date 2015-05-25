from django.conf.urls import include, url
from django.contrib import admin
from tricks import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tricks.urls')),

    # Url Entries for social auth
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    # Url Entries for django administration
    url(r'^account/', include('django.contrib.auth.urls', namespace='auth'))

    # url(r'^$', 'django_social_app.views.login'),
    # url(r'^home/$', 'django_social_app.views.home'),
    # url(r'^logout/$', 'django_social_app.views.logout'),

]
