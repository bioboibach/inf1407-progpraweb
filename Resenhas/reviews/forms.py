from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    product = forms.CharField(
        label="Produto ",
        widget=forms.TextInput(
            attrs={"class": "w-auto form-control", "placeholder": "Produto"}
        ),
    )
    brand = forms.CharField(
        label="Fabricante ",
        widget=forms.TextInput(
            attrs={"class": "w-auto form-control", "placeholder": "Fabricante"}
        ),
    )

    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
    score = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)

    
    content = forms.CharField(
        label="Conteúdo ",
        widget=forms.Textarea(
            attrs={"class": "w-auto form-control", "placeholder": "Conteúdo"}
        ),
    )
    product_url = forms.URLField(
        label="URL do Produto ",
        widget=forms.URLInput(
            attrs={"class": "w-auto form-control", "placeholder": "URL do Produto"}
        ),
    )

    class Meta:
        model = Review
        fields = ['product','brand', 'content', 'product_url','score']
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.RadioSelect(),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'product_url': forms.URLInput(attrs={'class': 'form-control'}),
        }