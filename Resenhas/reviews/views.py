
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
            "submitText": "Publicar",
        }
        return render(request, "reviews/review_form_create.html", contexto)
    
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
    
class ReviewUpdateView(View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(instance=review)
        return render(request, 'reviews/review_form_update.html', {'formulario': form, 'titulo': 'Atualizar Resenha', 'submitText': 'Atualizar'})
    
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:user-review-list')
        return render(request, 'reviews/review_form_update.html', {'formulario': form, 'titulo': 'Atualizar Resenha', 'submitText': 'Atualizar'})
    
class UserReviewListView(View):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.filter(author = get_user(request))
        
        contexto = {
            "reviews": reviews,
        }
        return render(request, "reviews/user_review_list.html", contexto)
    
class ReviewDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return redirect('reviews:user-review-list')

