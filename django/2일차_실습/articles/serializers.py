from rest_framework import serializers
from .models import Article, Comment, Topic


# 전체, 상세 데이터 조작 시 사용되는 필드가 동일하기 때문에
# 댓글 serializer 는 하나만 생성한다.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 조회는 괜찮은데, 생성할 때는 해당 필드는 빼고 생각해라!
        read_only_fields = ('article', )


# serializers.Serializer
# serializers.ModelSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


# 전체 데이터에 대한 serializer
class ArticleListSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'topics', )


# 상세 데이터에 대한 serializer
class ArticleSerializer(serializers.ModelSerializer):
    # Comment 내용 포함시키기
    # 1. CommentSerializer 활용하기
    # comment_set = CommentSerializer(many=True, read_only=True)

    # 2. 각 필드를 재정의
    # 필드명은 자유롭게 구성하면 된다
    # PrimaryKeyRelatedField: 참조하는 테이블의 PK
    # comment_id = serializers.PrimaryKeyRelatedField(source='comment_set', many=True, read_only=True)
    # comment_content = serializers.StringRelatedField(source='comment_set', many=True, read_only=True)

    # 3. SerializerMethodField
    comments = serializers.SerializerMethodField()

    # 자동으로 get_comments 메소드 호출
    # obj : instance
    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return [{
            'id': comment.id,
            'content': comment.content,
        } for comment in comments]


    class Meta:
        model = Article
        # all: 전체필드
        # -> 역참조 시 사용되는 필드명도 추가가 되어 있다. (comment_set) 
        fields = '__all__'


