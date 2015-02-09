from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import QuestionDetailView, ResultsView, vote

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="polls/index.html"), name='index'),
	url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>\d+)/vote/$', vote, name='vote'),
)