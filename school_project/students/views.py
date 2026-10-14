from django.shortcuts import render
from django.http import JsonResponse
from .models import Students
from rest_framework.response import Response
from rest_framework import status


def StudentsView(request):
  students = Students.objects.all().values()
  listed_students = list(students)
  return JsonResponse(listed_students, safe=False)


def DetailStudentView(request,pk):
  try:
    student = Students.objects.values().get(pk=pk)
    return JsonResponse(student, safe=False)
  except Students.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)