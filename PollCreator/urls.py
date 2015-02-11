from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<questionnaire_id>\d+)/$', views.detailQuestionnaire, name='detailQuestionnaire'),
    url(r'^NewQuestionnaire/$', views.newQuestionnaire, name='newQuestionnaire'),
    url(r'^AddQuestionnaire/$', views.addQuestionnaire, name='addQuestionnaire'),
    url(r'^NewQuestion/(?P<questionnaire_id>\d+)/$', views.newQuestion, name='newQuestion'),
    url(r'^AddQuestion/(?P<questionnaire_id>\d+)/$', views.addQuestion, name='addQuestion'),
    url(r'^NewChoice/(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/$', views.newChoice, name='newChoice'),
    url(r'^AddChoice/(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/$', views.addChoice, name='addChoice'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/$', views.detailQuestion, name='detailQuestion'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/results/$', views.resultsQuestion, name='resultsQuestion'),
    url(r'^(?P<questionnaire_id>\d+)/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)