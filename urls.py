from django.conf.urls import patterns, include, url
import settings
from controllers.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',upload , name="upload"),
    url(r'upload_file$',upload_file , name="upload_file"),
    # url(r'^incercare/', include('incercare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'static/(?P<path>.*)$','django.views.static.serve' ,{'document_root' : settings.MEDIA_ROOT},name="static"),
)
