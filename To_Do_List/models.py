from django.db import models

# Create your models here.

class To_Do_List(models.Model): #Table
  task = models.CharField(max_length=255)
  completed = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return self.task