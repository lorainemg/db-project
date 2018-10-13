from django.db import models


class Student(models.Model):
    first_name = models.CharField('nombre', max_length=30)
    last_name = models.CharField('apellidos', max_length=40)
    address = models.CharField('dirección', max_length=50)
    city = models.CharField('ciudad', max_length=20)
    email = models.EmailField('correo', blank=True, null=True)
    CI = models.IntegerField(default=0, primary_key=True)
    genre = (('F', 'Femenino'), ('M', 'Masculino'))
    sex = models.CharField(
        'sexo', max_length=2, choices=genre, default="F")
    telephone_number = models.IntegerField('teléfono', default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Secretary(models.Model):
    CIS = models.IntegerField(default=0, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    telephone_number = models.IntegerField(default=0, verbose_name='tel')
    work_zone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name


class ClassRoom(models.Model):
    IdC = models.IntegerField(default=0, primary_key=True)
    zone = models.CharField(max_length=30)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.IdC)


class Career(models.Model):
    name = models.CharField(max_length=30)
    career = models.IntegerField(default=0)
    kind = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TitleValidation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE)
    date = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return str(self.student) + " " + str(self.classroom)


class ValidatedStudent(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    secretary = models.ForeignKey(
        Secretary, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student) + " " + str(self.grade)


class ExamLocation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)


class Claim(models.Model):  #Reclamaciones
    student = models.ForeignKey(
        Student, on_delete="CASCADE")
    new_grade = models.IntegerField(default=0)

    def __str__(self):
        return str(self.student) + " " + str(self.new_grade)


class EstudianteAprobado(models.Model):  # pasar el nombre a ingles
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    career = models.ForeignKey(
        Career, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student) + " " + str(self.career)
