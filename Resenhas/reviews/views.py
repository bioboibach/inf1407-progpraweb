
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.contrib.auth import get_user,get_user_model
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy


# Create your views here.
from reviews.models import Review
from reviews.forms import ReviewForm

class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'reviews/review_list_all.html', {'reviews': reviews})
    
class ReviewCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {
            "formulario": ReviewForm,
            "titulo": "Escreva uma Resenha",
            "submitText": "Enviar",
        }
        return render(request, "reviews/review_form.html", contexto)
    
    def post(self, request):
        product = request.POST.get('product')
        content = request.POST.get('content')
        brand = request.POST.get('brand')
        product_url = request.POST.get('product_url')
        score = request.POST.get('score')
        author = get_user(request)
        post = Review(product=product, content=content, product_url=product_url, author=author, score=score, brand=brand)
        post.save()
        return HttpResponseRedirect(reverse_lazy('reviews:review-list'))