from django.shortcuts import render
from django.http import JsonResponse
from .models import Students


def StudentsView(request):
  students = Students.objects.all().values()
  listed_students = list(students)
  return JsonResponse(listed_students, safe=False)