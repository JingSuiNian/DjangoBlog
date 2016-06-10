from MyBlog.views import index
from django.conf.urls import patterns, include
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BlogNian.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       (r'^admin/', include(admin.site.urls)),
                       ('^index.html/$', index),
                       )
