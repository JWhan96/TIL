from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()    
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request, pk):
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    # CommentForm으로 사용자로부터 데이터를 입력받음
    # 댓글은 페이지 만드는 것과 달리 GET요청이 올일이 없으므로 이등분 하지 않는다.
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():

        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article.pk)      
    
    context={
        'article' : article,
        'comment_form' : comment_form,
        
    }

    return render(request, 'articles/detail.html', context)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)