from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Texto, Comment
from .forms import CommentForm


def home(request):
    return render(request, 'home.html')

@user_passes_test(lambda u: u.is_superuser, login_url='home')
def admin_page(request):
    return render(request, 'admin_page.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def add_comment(request, texto_id):
    texto = Texto.objects.get(pk=texto_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.texto = texto
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form, 'texto': texto})

def view_comments(request, texto_id):
    texto = Texto.objects.get(pk=texto_id)
    comentarios = Comment.objects.filter(texto=texto)
    return render(request, 'view_comments.html', {'texto': texto, 'comentarios': comentarios})

def add_comment_with_texto(request, texto_id):
    texto = Texto.objects.get(pk=texto_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.texto = texto
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form, 'texto': texto})
