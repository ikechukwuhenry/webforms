from django.conf.urls import include, url
from django.contrib import admin
import forms.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    url(r'^sharephoto$', 'forms.views.sharePhotos', name='sharePhotos'),
    url(r'^photos$', 'forms.views.album', name='photos'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
