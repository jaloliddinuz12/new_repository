from django.contrib import admin

from .models import Course, Student, Comment, Book

admin.site.register([Course, Student, Comment, Book])
