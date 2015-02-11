import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Questionnaire(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)