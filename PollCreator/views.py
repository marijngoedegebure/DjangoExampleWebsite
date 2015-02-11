from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from models import Choice, Question, Questionnaire
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext, loader


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'PollCreator/index.html'
    context_object_name = 'latest_questionnaire_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questionnaire.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


def newQuestion(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request, 'PollCreator/newQuestion.html', {'questionnaire': questionnaire})


def addQuestion(request, questionnaire_id):
    try:
        question_text = request.POST['question_text']
    except (KeyError, question_text.DoesNotExist):
        render(request, 'PollCreator/index.html')
    else:
        questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
        question = Question(question_text=question_text, questionnaire=questionnaire)
        question.save()
        questionnaire.save()
        return HttpResponseRedirect(reverse('PollCreator:detailQuestionnaire', args={questionnaire_id}))


def newChoice(request, questionnaire_id, question_id):
    question = get_object_or_404(Question, id=question_id)
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request, 'PollCreator/newChoice.html', {'questionnaire': questionnaire, 'question': question})


def addChoice(request, questionnaire_id, question_id):
    try:
        choice_text = request.POST['choice_text']
    except (KeyError, choice_text.DoesNotExist):
        render(request, 'PollCreator/index.html')
    else:
        question = get_object_or_404(Question, id=question_id)
        questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
        choice = Choice(choice_text=choice_text, question=question)
        choice.save()
        question.save()
        questionnaire.save()
        return HttpResponseRedirect(reverse('PollCreator:detailQuestion', args={questionnaire_id, question_id}))

def newQuestionnaire(request):
    return render(request, 'PollCreator/newQuestionnaire.html')


def addQuestionnaire(request):
    try:
        title = request.POST['title']
    except (KeyError, title.DoesNotExist):
        render(request, 'PollCreator/index.html')
    else:
        questionnaire = Questionnaire(title=title, pub_date=timezone.now())
        questionnaire.save()
        return HttpResponseRedirect(reverse('PollCreator:index'))


def detailQuestion(request, questionnaire_id, question_id):
    question = get_object_or_404(Question, id=question_id)
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request, 'PollCreator/detailQuestion.html', {'questionnaire': questionnaire, 'question': question})


def detailQuestionnaire(request, questionnaire_id):
    try:
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
    except Questionnaire.DoesNotExist:
        raise Http404("No Questionnaire matches the given query.")
    return render(request, 'PollCreator/detailQuestionnaire.html', {'questionnaire': questionnaire})


def resultsQuestion(request, questionnaire_id, question_id):
    question = get_object_or_404(Question, id=question_id)
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request, 'PollCreator/resultsQuestion.html', {'questionnaire': questionnaire, 'question': question})

def vote(request, questionnaire_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'PollCreator/detailQuestion.html', {
            'questionnaire': questionnaire,
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('PollCreator:resultsQuestion', args=(questionnaire_id, question.id,)))