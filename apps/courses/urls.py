from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'modules', ModuleViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
