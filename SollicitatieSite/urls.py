from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from PollCreator.models import Questionnaire, Question
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('title', 'pub_date')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'questionnaire')

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# ViewSets define the view behavior.
class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'questionnaire', QuestionnaireViewSet)
router.register(r'question', QuestionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^PollCreator/', include('PollCreator.urls', namespace="PollCreator")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
