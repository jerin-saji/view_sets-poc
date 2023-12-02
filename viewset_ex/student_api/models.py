from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    age = models.IntegerField()
    # Add any other fields you need

    def __str__(self):
        return self.name
