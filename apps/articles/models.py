from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, help_text="Short summary of the article")
    thumbnail = models.ImageField(upload_to='articles/', null=True, blank=True)
    category = models.CharField(max_length=100) # Or ForeignKey to a Topic model if we want topics separate
    author = models.CharField(max_length=100, default="Tim ResikPlus")
    is_featured = models.BooleanField(default=False)
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Scheduled', 'Scheduled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    views = models.PositiveIntegerField(default=0)
    tags = models.JSONField(default=list, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
