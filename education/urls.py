from django.urls import path
from .views import TopicPublicViewSet, ArticlePublicViewSet, ArticleAdminViewSet

urlpatterns = [
    # path("topics/<slug:slug>/", TopicDetailView.as_view(), name="topic-detail"),
    path("topics/", TopicPublicViewSet.as_view({"get": "list"}), name="topic-list"),
    path("articles/<slug:slug>/", ArticlePublicViewSet.as_view({"get": "retrieve"}), name="article-detail"),
    path("articles/", ArticlePublicViewSet.as_view({"get": "list"}), name="article-list"),
]
