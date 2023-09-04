from django.shortcuts import render
from .models import News

def main(request):
    a = News.objects.all()
    context = {'queryset' : a}
    return render(request, 'index.html', context)

def content(request):
    ...

