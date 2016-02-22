"""Request received for this app will be handled here."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail,\
        name='review_detail'),
    # ex: /wine/
    url(r'^Hotel$', views.Hotel_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^Hotel/(?P<Hotel_id>[0-9]+)/$', views.Hotel_detail, \
        name='Hotel_detail'),
]
