from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer, IsAuthorOrReadOnly



from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .models import Student
from .serializers import StudentSerializer
from rest_framework import permissions




class StudentListAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            students = Student.objects.filter(course_id=course_id)
        else:
            students = Student.objects.all()
        return students


    def get_serializer_class(self):
        # if self.request.user.is_staff:
        #     return StudentSerializerForAdmin
        return StudentSerializer


class StudentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "student_id"
    permission_classes = [permissions.IsAdminUser]



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class StudentAPIView(APIView):
#     def get(self, request: Request, pk: int = None):
#         if pk is None:
#             students = Student.objects.all()
#             serializer = StudentSerializer(students, many=True)
#             return Response(serializer.data)
#         else:
#             student = get_object_or_404(Student, pk=pk)
#             return Response(StudentSerializer(student).data)
#
#     def post(self, request, pk: int = None):
#         if pk:
#             return Response({"message": "Method POST not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         student = serializer.save()
#         return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request, pk: int = None):
#         if not pk:
#             return Response({"message": "Method PUT not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(data=request.data, instance=student)
#         serializer.is_valid(raise_exception=True)
#         return Response(StudentSerializer(serializer.save()).data)
#
#     def delete(self, request, pk: int = None):
#         if not pk:
#             return Response({"message": "Method DELETE not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#         return Response({"message": "Student deleted successful"}, status=status.HTTP_204_NO_CONTENT)