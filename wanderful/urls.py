from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wanderful.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', 'wander.views.test', name='test'),
    url(r'^home/$', 'wander.views.home', name='home'),
    url(r'^profile/$', 'wander.views.profile', name='profile'),
    url(r'^register/$', 'wander.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^locations/(?P<category_id>\w+)/$', 'wander.views.locations', name='locations'),
    url(r'^location/new/$', 'wander.views.location_new', name='location_new'),
    url(r'^category/new/$', 'wander.views.category_new', name='category_new'),
    url(r'^categories/$', 'wander.views.categories', name='categories'),
    url(r'^map/(?P<location_id>\w+)/$', 'wander.views.map', name='map'),

)
