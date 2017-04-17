from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib import admin
from open_news import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
   	url(r'^$', views.article_list, name="vegasliving")
]
