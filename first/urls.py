from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myProfile/',include('myProfile.urls')),
    url(r'^$', views.showHome),
]

urlpatterns += staticfiles_urlpatterns()
