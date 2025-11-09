from django.shortcuts import render, redirect
from .forms import QuestionForm

from django.http import HttpResponse

def index(request):
    return HttpResponse("Inquiry app is working!")

def question_form(request):
    return render(request, 'inquiry/question_form.html')

def question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inquiry/thanks.html')
    else:
        form = QuestionForm()

    return render(request, 'inquiry/question_form.html', {'form': form})