from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    durations = models.SmallIntegerField(default=4)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, default="+998991234567")
    birth_year = models.SmallIntegerField(default=2010)
    image = models.ImageField(upload_to="images/students/", null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" yozgan odam {self.author.username} blan kitobi {self.book.title}"
