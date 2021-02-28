from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    """ Student user """

    student_id  = models.IntegerField(blank=False)
    first_name  = models.CharField(max_length=250, blank=False)
    last_name   = models.CharField(max_length=250, blank=False)
    email       = models.CharField(max_length=250, blank=False)
    password    = models.CharField(max_length=500, blank=False)
    is_student  = models.BooleanField(default=True)

    #* OneToOne Relationship
    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

class Coordinator(models.Model):
    """ Coordinator user """

    coordinator_id  = models.IntegerField(blank=False)
    first_name      = models.CharField(max_length=250, blank=False)
    last_name       = models.CharField(max_length=250, blank=False)
    email           = models.CharField(max_length=250, blank=False)
    password        = models.CharField(max_length=500, blank=False)
    position        = models.CharField(max_length=500, blank=False)
    is_coordinator  = models.BooleanField(default=True)

    #* OneToOne Relationship
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=False)