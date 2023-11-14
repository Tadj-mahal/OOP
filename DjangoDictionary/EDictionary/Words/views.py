from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import WordForm
from .models import Word

class MainView(TemplateView):
    template_name = "index.html"
    def get(self, request):
        return render(request, self.template_name)

class WordsAdding(TemplateView):
    template_name = "add_word.html"
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        form = WordForm(request.POST)
        context = {}
        if form.is_valid():
            form.save()
            context = {
                'success': "Word successfully added.",
            }
        else:
            context['form'] = form

        return render(request, self.template_name, context)

class WordsList(TemplateView):
    def get(self, request):
        words = Word.objects.all()
        context = {
            'words': words,
        }
        return render(request, "words_list.html", context)