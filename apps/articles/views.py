from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = []
    # lookup_field = 'slug' # Removed to align with frontend using ID

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def topics(self, request):
        # Return unique categories/topics
        topics = self.queryset.values_list('category', flat=True).distinct()
        # Format as expected by frontend: { id: str, name: str, count: int } maybe? 
        # Frontend education.ts expects just list of topics? 
        # Let's check frontend expects: getTopics returns res.data. 
        # Assuming simple list or list of objects.
        # Let's return a list of objects for now.
        data = [{"name": t} for t in topics]
        return Response(data)
