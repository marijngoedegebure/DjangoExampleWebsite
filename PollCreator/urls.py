from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<questionnaire_id>\d+)/$', views.detailQuestionnaire, name='detailQuestionnaire'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/$', views.detailQuestion, name='detailQuestion'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/results/$', views.resultsQuestion, name='resultsQuestion'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)