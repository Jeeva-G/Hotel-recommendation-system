"""This file has regular expressions to parse & redirect apps request."""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'HotelsReco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin/', include(admin.site.urls)),
]
