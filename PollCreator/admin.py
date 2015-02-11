from django.contrib import admin
from PollCreator.models import Question, Choice, Questionnaire

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Questionnaire)