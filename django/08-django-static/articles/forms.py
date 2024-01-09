from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class ArticledetailForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)
