from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def detail(request, question_id):
    return HttpResponse(f"você está olhando para a questão {question_id}")

def results(request, question_id):
    response = f"você está olhando para os resultados da questão {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"você está votando na questão {question_id}")
