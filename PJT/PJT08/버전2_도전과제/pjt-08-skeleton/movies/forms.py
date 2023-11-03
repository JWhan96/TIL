from django import forms
from .models import Genre, Movie

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'