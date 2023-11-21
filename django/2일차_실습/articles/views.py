import json
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, TopicSerializer
from .models import Article, Topic


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # 쿼리셋을 json 형태로 포장
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data.get('topics'))) # 문자열이다!
        topics_string = request.data.get('topics')
        topics_data = json.loads(topics_string)
        
        # topics_data 반복하면서
        # 1. TOPIC 테이블에 새로운 토픽이라면 추가
        # 2. 기존에 있다면, 저장은 하지 않음
        # 3. 기존에 있던 없던 생성하려던 게시글과는 관계를 설정해줘야한다.

        # 비어있는 리스트
        topics = []
        # topics_data: 리스트
        # topic: 문자열
        for topic in topics_data:
            # 토픽 데이터를 딕셔너리로 정의
            topic_data = { "name": topic }
            topic_serializer = TopicSerializer(data=topic_data)
            # 존재하면 exist_topic 변수에 담김
            exist_topic = Topic.objects.filter(name=topic).first()
            if exist_topic:
                # 관계 설정을 위해 비어있는 리스트에 추가
                topics.append(exist_topic)
            else:
                # 없다면 생성
                if topic_serializer.is_valid(raise_exception=True):
                    topic_serializer.save()
                    # 생성한 인스턴스를 리스트에 추가
                    topics.append(topic_serializer.instance)
        
        
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article = serializer.save()

            # article - topics 관계 설정
            # set: 여러 개의 데이터를 한 번에 관계를 지어줌
            article.topics.set(topics)

            # 이렇게만 적으면 조회랑 구별이 안됨
            # return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 없는 데이터를 조회하면 버그난다!
    # article = Article.objects.get(pk=article_pk)

    # 버그가 아닌, 에러 상태를 잘 돌려줘야 한다.
    # try:
    #     article = Article.objects.get(pk=article_pk)
    # except Article.DoesNotExist:
    #     return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

    # 쉬운 방법
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        # 조회 수 추가
        serializer = ArticleSerializer(article)

        article.views += 1
        article.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        # 삭제 메세지를 주고 싶으면 아래와 같이 작성
        return Response({'message': "삭제 완료"}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # partial=True : 수정 시 특정 필드만 입력받고 싶을 때
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    if request.method == 'GET':
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)