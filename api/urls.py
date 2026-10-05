from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (StudentListAPIView, StudentRetrieveAPIView, CommentViewSet)

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
urlpatterns = [
    path('students/', StudentListAPIView.as_view()),
    path('students/course/<int:course_id>/', StudentListAPIView.as_view()),
    path('students/<int:student_id>/', StudentRetrieveAPIView.as_view()),
    path('', include(router.urls)),
]

