from django.db import models
from django.utils import timezone

class Course(models.Model):
    LEVEL_CHOICES = (
        ('Pemula', 'Pemula'),
        ('Menengah', 'Menengah'),
        ('Lanjutan', 'Lanjutan'),
    )
    TYPE_CHOICES = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    )
    STATUS_CHOICES = (
        ('Aktif', 'Aktif'),
        ('Draft', 'Draft'),
        ('Coming Soon', 'Coming Soon'),
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    instructor = models.CharField(max_length=255, default="Instruktur ResikPlus")
    duration = models.CharField(max_length=50, help_text="e.g. 4 minggu")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Pemula')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    features = models.JSONField(default=list, help_text="List of features")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Online')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    students_count = models.IntegerField(default=0)
    lessons_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    TYPE_CHOICES = (
        ('video', 'Video'),
        ('document', 'Document'),
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment'),
    )
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='video')
    duration = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 10:30")
    content = models.TextField(blank=True, null=True, help_text="URL, text content, or quiz config")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.title} - {self.title}"

class CourseRegistration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.course.title}"
