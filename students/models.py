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
