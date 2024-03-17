from django.db import models
# Create your models here.


class Faculity(models.Model):
    """ Факультет """
    name = models.CharField(max_length=200)
    

class Group(models.Model):
    """ Группа """
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    # При удалении факультета группа остаётся с нулевой ссылкой
    facility_id = models.ForeignKey(Faculity, on_delete=models.SET_NULL, null=True)


class User(models.Model):
    """ Пользователь """
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    group_name = models.CharField(max_length=200, null=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    VK_ID = models.CharField(max_length=200, null=True)
    role_id = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

class Course(models.Model):
    """ Курс в базе данных"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class User_course(models.Model):
    """ Пользователи и их курсы """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class Content(models.Model):
    """ Содержимое курса (файл) """
    path = models.CharField(max_length=200)
    ctype = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    # При удалении автора или курса содержимое существует с нулевой ссылкой
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


