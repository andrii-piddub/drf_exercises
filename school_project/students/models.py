from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField(max_length=10)
  email = models.EmailField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name
  
