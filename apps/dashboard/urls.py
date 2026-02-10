from django.urls import path
from .views import DashboardStatsView, RecentActivitiesView, TopPartnersView

urlpatterns = [
    path('stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('recent-activities/', RecentActivitiesView.as_view(), name='recent-activities'),
    path('top-partners/', TopPartnersView.as_view(), name='top-partners'),
]
