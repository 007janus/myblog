from django.conf.urls import include, url
from django.contrib import admin
from myblog import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', views.index)
]
