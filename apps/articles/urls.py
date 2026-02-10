from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet) # /api/education/articles/

urlpatterns = [
    path('topics/', ArticleViewSet.as_view({'get': 'topics'}), name='topics-list'),
    path('', include(router.urls)),
]
