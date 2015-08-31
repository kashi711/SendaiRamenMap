from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf.urls import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practice2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'myapp.views.index', name='root'),
    url(r'^index/$', 'myapp.views.index', name='index'),
    url(r'^result/$', 'myapp.views.result', name='result'),
    url(r'^login/$', 'myapp.views.loginpage', name='loginpage'),
    url(r'^loginpage_error/$', 'myapp.views.loginpage_error', name='loginpage_error'),
    url(r'^enter/$', 'myapp.views.enter',name='enter'),
    url(r'^make/$', 'myapp.views.make', name='make'),
    url(r'^make_error1/$', 'myapp.views.make_error1', name='make_error1'),
    url(r'^make_error2/$', 'myapp.views.make_error2', name='make_error2'),
    url(r'^makeAccount/$', 'myapp.views.makeAccount', name='makeAccount'),
    url(r'^out/$', 'myapp.views.out', name='out'),
    url(r'^similarity/(?P<shop_id>\d+)/$', 'myapp.views.similarity', name='similarity'),
    url(r'^detail/(?P<shop_id>\d+)/$', 'myapp.views.detail', name='detail'),
    url(r'^detail_more/(?P<shop_id>\d+)/$', 'myapp.views.detail_more', name='detail_more'),
    url(r'^preserve/(?P<shop_id>\d+)/$', 'myapp.views.preserve', name='preserve'),
    url(r'^post/(?P<shop_id>\d+)/$', 'myapp.views.post', name='post'),
    url(r'^delete/(?P<shop_id>\d+)/$', 'myapp.views.delete', name='delete'),
    url(r'^edit/(?P<shop_id>\d+)/$', 'myapp.views.edit', name='edit'),
    #url(r'^admin/', include(admin.site.urls)),
)
