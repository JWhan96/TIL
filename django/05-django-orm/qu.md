### QuerySet API 를 위한 외부 라이브러리
1. pip install ipython
2. pip install django-extensions

### django shell 실행
- python manage.py shell_plus
- 나가려면 exit 입력
### 첫번쨰 작성방법
- article.title
- (article클래스).(title)
- article.save()를 해야 최종적으로 DB에 저장된다
- 모든 값 조회Article.objects.all() (쿼리셋)
- id조회는 article.pk = article.id
```py
In [2]: article = Article()

In [3]: article
Out[3]: <Article: Article object (None)>

In [4]: article.title = 'first title'

In [5]: article
Out[5]: <Article: Article object (None)>

In [6]: article.title
Out[6]: 'first title'

In [7]: article.content = 'django!'

In [8]: article
Out[8]: <Article: Article object (None)>

In [9]: article.content
Out[9]: 'django!'

In [10]: article.save()

In [11]: article
Out[11]: <Article: Article object (1)>
```
### 두번째 작성 방법
- article = Article(title = 'second', content = 'django')
### 세번쨰 작성 방법
- Article.objects.create(title= 'third', content = 'django!') 
- 이 방법만 save()기능이 자동으로 진행

## 조회
```py
articles = Article.objects.all()
for article in articles:
    ...:     print(article.title)
# 결과 
# first title
# second
# third
```
```py
# get 메서드는 하나만 리턴 가능 여러개 리턴하면 오류남
# pk에 적합한 메서드(다른건 같은 게 겹칠 수 있기 때문에)
In [13]: Article.objects.get(pk = 1)
Out[13]: <Article: Article object (1)>
```
```py
# filter 메서드는 여러가지 자료를 찾는데 적합

In [15]: Article.objects.filter(content = 'django!')
Out[15]: <QuerySet [<Article: Article object (1)>, <Article: Article object (3)>]>
# 없는 자료를 찾더라도 오류가 나지는 않음 빈값 반환
In [17]: Article.objects.filter(content = 'do!')
Out[17]: <QuerySet []>
# 하나의 값만 있더라도 queryset으로 반환
In [18]: Article.objects.filter(title = 'second')
Out[18]: <QuerySet [<Article: Article object (2)>]>
```
- Field lookups(포함되어있는지)
```py
In [23]: Article.objects.filter(content__contains = 'an')
Out[23]: <QuerySet [<Article: Article object (2)>, <Article: Article object (3)>]>
```


## 수정
- 수정을 하려면 조회가 필수
```py
In [19]: article = Article.objects.get(pk = 1)

In [20]: article.title = 'first change'

In [21]: article.save()
```

## 삭제

```py
In [19]: article = Article.objects.get(pk = 1)
In [22]: article.delete()
Out[22]: (1, {'articles.Article': 1})
# 전부 삭제하는방법
articles = Article.objects.all()
articles.delete()
```






## 질문
왜 article에 title이랑 content등록할 때는 article이고
Article.objects.all()에서는 대문자 인가
- 왜 타이틀은 마지막 것만 뜨는것인가
#### 참고
- terminal 화면 깨끗하게 만드는 법 ctrl + L(입력창을 맨위로)