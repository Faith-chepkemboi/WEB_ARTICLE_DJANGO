
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

from django.http import JsonResponse

from django.shortcuts import redirect

def home(request):
    return redirect('login')  




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
          form = AuthenticationForm()
          return render(request, 'myapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'myapp/dashboard.html', {'articles': articles})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'myapp/create_article.html', {'form': form})

# def search_articles(request):
#     query = request.GET.get('q')
#     articles = Article.objects.filter(title__icontains=query)
#     return render(request, 'myapp/search_results.html', {'articles': articles, 'query': query})

def search_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query)
    if request.is_ajax():
        articles_data = list(articles.values('title', 'preview'))
        return JsonResponse({'articles': articles_data})
    return render(request, 'myapp/search_results.html', {'articles': articles, 'query': query})

