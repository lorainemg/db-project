from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True, verbose_name='e-mail')
    ci = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Secretary(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    telefon_number = models.IntegerField(default=0, verbose_name='tel')
    work_zone = models.CharField(max_length=20)
    student = models.ForeignKey(
        Student, on_delete='CASCADE', blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class ClassRoom(models.Model):
    number = models.IntegerField(default=0)
    zone = models.CharField(max_length=30)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.number


class Career(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField(default=0)
    kind = models.CharField(max_length=30)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name
