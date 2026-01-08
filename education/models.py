from django.db import models
from django.utils.text import slugify

### EDUCATIONAL CONTENT MODELS ###
class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(
        max_length=50,
        help_text="Nama icon lucide-react (Leaf, Recycle, Trash2, dll)"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Article(models.Model):
    topic = models.ForeignKey(
        Topic,
        related_name="articles",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
