from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import NewPostForm
from .models import Post


def index(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            post = Post(text=data['text'])
            post.save() 
            return redirect(index)

    template = loader.get_template('index.html')
    posts = Post.objects.all()
    form = NewPostForm()
    context = {'form': form, 'posts': posts}
    return HttpResponse(template.render(context, request))
