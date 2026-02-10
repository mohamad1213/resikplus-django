from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 
            'thumbnail', 'category', 'author', 'is_featured', 'status',
            'views', 'tags',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'slug']

    def to_internal_value(self, data):
        # Handle tags being sent as a JSON string in multipart/form-data
        # Convert QueryDict to standard dict to handle arbitrary types (like list from JSON)
        if hasattr(data, 'dict'):
             data = data.dict()
        elif hasattr(data, 'copy'):
             data = data.copy()

        if 'tags' in data and isinstance(data['tags'], str):
            import json
            try:
                data['tags'] = json.loads(data['tags'])
            except ValueError:
                pass 
        return super().to_internal_value(data)
