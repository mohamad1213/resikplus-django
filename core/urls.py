from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
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
