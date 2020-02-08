from django.shortcuts import render,redirect
from django.http import JsonResponse
from .utils import random_word_display

def home(request):
    return render(request,'home.html')

def authenticate(request):
    if request.method == 'POST':
        password = request.POST['password']
        if password == 'abcdef':
            return JsonResponse({'success':True},status=200)
    return JsonResponse({'success':False},status=500)

def question(request):
    word = random_word_display()
    return render(request,'question.html',{'word':word})

            
        