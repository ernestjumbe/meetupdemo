from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meetupdemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^polls/', include('polls.urls', namespace='polls', app_name='polls')),
    url(r'^twitter/$', TemplateView.as_view(template_name='tweets.html'), name='twitter'),
    url(r'^admin/', include(admin.site.urls)),
)
