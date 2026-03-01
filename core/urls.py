from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from apps.courses.views import ModuleViewSet, LessonViewSet, CourseRegistrationViewSet

router = DefaultRouter()
router.register(r'modules', ModuleViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'course-registrations', CourseRegistrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/courses/", include("apps.courses.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/education/", include("apps.articles.urls")),
    path("api/partners/", include("apps.partners.urls")),
    path("api/", include("apps.waste_pickups.urls")),
    path("api/dashboard/", include("apps.dashboard.urls")),
    path("api/accounts/", include("apps.accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
