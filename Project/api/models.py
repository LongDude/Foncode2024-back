from django.db import models
# Create your models here.


class User(Model.model):
    """ Пользователь """
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
    """ Пользователи и их курсы """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class Course(Model.model):
    """ Курс в базе данных"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Content(Model.model):
    """ Содержимое курса (файл) """
    path = models.CharField(max_length=200)
    ctype = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    # При удалении автора или курса содержимое существует с нулевой ссылкой
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)

class Group(Model.model):
    """ Группа """
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    # При удалении факультета группа остаётся с нулевой ссылкой
    facility_id = model.ForeignKey(Faculity, on_delete=models.SET_NULL)

class Faculity(Model.model):
    """ Факультет """
    name = models.CharField(max_length=200)
    