from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Topic, Article
from .serializers import TopicSerializer, ArticleListSerializer, ArticleDetailSerializer, AdminArticleSerializer
# PUBLIC
class TopicPublicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    http_method_names = ["get"]
    permission_classes = [AllowAny]


class ArticlePublicViewSet(ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ArticleDetailSerializer
        return ArticleListSerializer

    http_method_names = ["get"]
    permission_classes = [AllowAny]

# ADMIN
class ArticleAdminViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = AdminArticleSerializer
    permission_classes = [IsAdminUser]

