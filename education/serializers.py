from rest_framework import serializers
from .models import Topic, Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "excerpt",
            "is_featured",
            "created_at",
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "topic",
            "created_at",
        ]


class TopicSerializer(serializers.ModelSerializer):
    articles = ArticleListSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "icon",
            "articles",
        ]

class AdminArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"