from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from django.views.decorators.http import require_GET



def StudentsView(request):
  students = Student.objects.all().values()
  listed_students = list(students)
  return JsonResponse(listed_students, safe=False)

@require_GET
def DetailStudentView(request,pk):
  try:
    student = Student.objects.values().get(pk=pk)
    return JsonResponse(student, safe=False)
  except Student.DoesNotExist:
    return JsonResponse({'error': 'Student not found'}, status=404)