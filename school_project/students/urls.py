from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentsView),
    path('<int:pk>/',views.DetailStudentView),

]
