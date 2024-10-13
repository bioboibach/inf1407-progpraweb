
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.contrib.auth import get_user,get_user_model
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy


# Create your views here.
from posts.models import Post
from posts.forms import PostForm

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/post_list_all.html', {'posts': posts})
    
class PostCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {
            "formulario": PostForm,
            "titulo": "Escreva uma Resenha",
            "submitText": "Enviar",
        }
        return render(request, "posts/post_form.html", contexto)
    
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        product_url = request.POST.get('product_url')
        author = get_user(request)
        post = Post(title=title, content=content, product_url=product_url, author=author)
        post.save()
        return HttpResponseRedirect(reverse_lazy('posts:post-list'))