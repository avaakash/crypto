from django.shortcuts import render,redirect
from django.http import JsonResponse
from .utils import random_word_display
from .models import Words

def home(request):
    return render(request,'home.html')

def authenticate(request):
    if request.method == 'POST':
        password = request.POST['password']
        if password == 'abcdef':
            word = random_word_display()
            request.session['word_key'] = word.key
            return JsonResponse({'success':True},status=200)
    return JsonResponse({'success':False},status=500)

def question(request):
    if 'word_key' in request.session:
        word = Words.objects.get(key=request.session['word_key']) 
        return render(request,'question.html',{'word':word})
    return redirect('home')
        