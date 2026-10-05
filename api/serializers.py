from rest_framework import serializers, permissions

from .models import Student, Comment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'image': {'write_only': True}}


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'book', 'author', 'text', 'created_at']



    # class StudentSerializerForAdmin(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'



# class StudentSerializer(serializers.Serializer):
#     id = serializers.BigIntegerField(read_only=True)
#     full_name = serializers.CharField(max_length=255)
#     phone_number = serializers.CharField(max_length=13, default="+998991234567")
#     birth_year = serializers.IntegerField(default=2010)
#     image = serializers.ImageField(required=False)
#     address = serializers.CharField(max_length=255)
#     course_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance: Student, validated_data):
#         instance.full_name = validated_data.get("full_name", instance.full_name)
#         instance.phone_number = validated_data.get("phone_number", instance.phone_number)
#         instance.birth_year = validated_data.get("birth_year", instance.birth_year)
#         instance.address = validated_data.get("address", instance.address)
#         instance.course_id = validated_data.get("course_id", instance.course_id)
#         instance.save()
#         return instance