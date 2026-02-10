from rest_framework.views import APIView
from rest_framework.response import Response
from apps.accounts.models import User
from apps.products.models import Product
from apps.partners.models import Partner
from apps.waste_pickups.models import WastePickup
from apps.articles.models import Article
from apps.courses.models import Course
from django.db.models import Sum

class DashboardStatsView(APIView):
    def get(self, request):
        total_users = User.objects.count()
        total_products = Product.objects.count()
        total_partners = Partner.objects.count()
        total_articles = Article.objects.count()
        total_courses = Course.objects.count()
        
        waste_stats = WastePickup.objects.filter(status='completed').aggregate(
            total_weight=Sum('actual_weight')
        )
        total_recycled = waste_stats['total_weight'] or 0
        
        return Response({
            "total_users": total_users,
            "total_products": total_products,
            "total_partners": total_partners,
            "total_recycled": total_recycled,
            "total_articles": total_articles,
            "total_courses": total_courses
        })
        print(response)

class RecentActivitiesView(APIView):
    def get(self, request):
        activities = []
        
        # Latest users
        latest_users = User.objects.order_by('-date_joined')[:3]
        for user in latest_users:
            activities.append({
                "id": f"u-{user.id}",
                "action": "Pengguna baru mendaftar",
                "user": user.get_full_name or user.email,
                "time": user.date_joined.strftime("%Y-%m-%d %H:%M"),
                "timestamp": user.date_joined
            })

        # Latest products
        latest_products = Product.objects.order_by('-created_at')[:3]
        for product in latest_products:
             activities.append({
                "id": f"p-{product.id}",
                "action": "Produk baru ditambahkan",
                "user": product.name,
                "time": product.created_at.strftime("%Y-%m-%d %H:%M"),
                "timestamp": product.created_at
            })

        # Latest articles
        latest_articles = Article.objects.order_by('-created_at')[:3]
        for article in latest_articles:
             activities.append({
                "id": f"a-{article.id}",
                "action": "Artikel baru diterbitkan",
                "user": article.title,
                "time": article.created_at.strftime("%Y-%m-%d %H:%M"),
                "timestamp": article.created_at
            })

        # Latest courses
        latest_courses = Course.objects.order_by('-created_at')[:3]
        for course in latest_courses:
             activities.append({
                "id": f"c-{course.id}",
                "action": "Kursus baru dibuat",
                "user": course.title,
                "time": course.created_at.strftime("%Y-%m-%d %H:%M"),
                "timestamp": course.created_at
            })
            
        # Sort by timestamp
        activities.sort(key=lambda x: x['timestamp'], reverse=True)
        
        # Return top 5
        return Response(activities[:5])

class TopPartnersView(APIView):
    def get(self, request):
        # We can aggregate waste pickup weight by partner
        partners = Partner.objects.annotate(
            total_recycled=Sum('waste_pickups__actual_weight')
        ).order_by('-total_recycled')[:5]
        
        data = []
        total_all_partners = sum(p.total_recycled or 0 for p in partners)
        
        for partner in partners:
            weight = partner.total_recycled or 0
            percentage = (weight / total_all_partners * 100) if total_all_partners > 0 else 0
            data.append({
                "name": partner.name,
                "recycled": f"{weight} kg",
                "percentage": round(percentage, 1)
            })
            
        return Response(data)
