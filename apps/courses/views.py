from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from apps.accounts.models import User
from .models import Course, Module, Lesson, CourseRegistration
from .serializers import CourseSerializer, ModuleSerializer, LessonSerializer, CourseRegistrationSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-created_at')
    serializer_class = CourseSerializer
    permission_classes = [] 

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_courses(self, request):
        registrations = CourseRegistration.objects.filter(user=request.user, status='berhasil')
        courses_data = []
        for reg in registrations:
            course = reg.course
            serializer = CourseSerializer(course, context={'request': request})
            data = serializer.data
            data['course_status'] = 'in_progress'
            data['progress'] = 0
            # Get next lesson safely
            next_lesson_str = '-'
            if course.modules.exists():
                first_module = course.modules.order_by('order').first()
                if first_module and first_module.lessons.exists():
                    first_lesson = first_module.lessons.order_by('order').first()
                    next_lesson_str = f"{first_module.title}: {first_lesson.title}"
                elif first_module:
                    next_lesson_str = f"{first_module.title}"
                    
            data['next_lesson'] = next_lesson_str
            data['completed_modules'] = 0
            data['enrolled_at'] = reg.created_at
            courses_data.append(data)
            
        return Response(courses_data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        course = self.get_object()
        email = request.data.get('email')
        
        if CourseRegistration.objects.filter(course=course, email=email).exists():
            return Response({"detail": "Email ini sudah terdaftar untuk kursus ini."}, status=status.HTTP_400_BAD_REQUEST)
            
        existing_user = User.objects.filter(email=email).first()
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            if existing_user:
                generated_password = "Sudah punya akun"
            else:
                generated_password = f"ResikPlus@{get_random_string(5)}"
                
            serializer.save(course=course, generated_password=generated_password)
            
            response_data = serializer.data
            response_data['generated_password'] = generated_password
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all().order_by('order')
    serializer_class = ModuleSerializer
    permission_classes = []
    
    def get_queryset(self):
        queryset = super().get_queryset()
        course_id = self.request.query_params.get('course')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('order')
    serializer_class = LessonSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        module_id = self.request.query_params.get('module')
        if module_id:
            queryset = queryset.filter(module_id=module_id)
        return queryset

class CourseRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CourseRegistration.objects.all().order_by('-created_at')
    serializer_class = CourseRegistrationSerializer
    permission_classes = []
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        registration = self.get_object()
        if registration.status == 'berhasil':
            return Response({"detail": "Status sudah berhasil."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user already exists
        existing_user = User.objects.filter(email=registration.email).first()
        plain_password = None
        
        if existing_user:
            registration.user = existing_user
        else:
            plain_password = registration.generated_password
            if not plain_password or plain_password == "Sudah punya akun":
                plain_password = f"ResikPlus@{get_random_string(5)}"
                registration.generated_password = plain_password
            
            new_user = User.objects.create_user(
                email=registration.email,
                password=plain_password,
                is_active=True,
                is_verified=True,
                is_staff=False,
                is_superuser=False,
            )
            registration.user = new_user

        registration.status = 'berhasil'
        registration.save()
        
        return Response({
            "detail": "Berhasil disetujui.",
            "email": registration.email,
            "password": plain_password if plain_password else "Sudah punya akun",
            "course": registration.course.title
        }, status=status.HTTP_200_OK)
