from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.db.models import F

# Create your views here.
def index(request):
    lista_ultimas_questoes = Question.objects.order_by("-pub_date")[:5]
    context = {"lista_ultimas_questoes": lista_ultimas_questoes}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = f"você está olhando para os resultados da questão {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        opcao_selecionada = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request, "polls/detail.html",{
                "question": question,
                "error_menssage": "você não selecionou uma opção",
            },
        )
    else:
        opcao_selecionada.votes = F("votes") + 1
        opcao_selecionada.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})