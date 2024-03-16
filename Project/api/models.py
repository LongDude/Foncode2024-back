from django.db import models
# Create your models here.


class User(Model.model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    group_name = models.CharField(max_length=200)
    group_id = models.PositiveIntegerField()
    VK_ID = models.CharField(max_length=200)
    role_id = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

class User_course(Model.model):
    user_id = models.PositiveIntegerField()
    course_id = models.PositiveIntegerField()

class Course(Model.model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Content(Model.model):
    path = models.CharField(max_length=200)
    ctype = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    course_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

class Group(Model.model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    facility_id = model.PositiveIntegerField()

class Faculity(Model.model):
    name = models.CharField(max_length=200)
    