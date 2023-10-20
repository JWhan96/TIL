from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=(
        ('Comedy', 'Comedy'),
        ('Fantasy', 'Fatasy'),
        ('Romance', 'Romance'),
    ))
    rating = forms.FloatField(min_value=0, max_value=5, step_size=0.5)
    
    class Meta:
        model = Movie
        fields = ('title', 'content',  'genre', 'rating' )        
        exclude = ('user', 'like_users',)

        labels = {
            'title' : '제목',
            'content' : '내용',
            'genre' : '장르',
            'rating' : '평점' ,
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
