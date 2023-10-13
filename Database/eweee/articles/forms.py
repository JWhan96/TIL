from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=(
        ('comedy', '코미디'),
        ('fantasy', '판타지'),
        ('romance', '로맨스'),
    ))
    rating = forms.FloatField(min_value=0, max_value=5, step_size=0.5)
    
    class Meta:
        model = Article
        fields = ('title', 'content',  'genre', 'rating' )        
        exclude = ('user',)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
