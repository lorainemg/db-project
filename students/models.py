from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    CI = models.IntegerField(default=0, primary_key=True)
    first_name = models.CharField('nombre', max_length=30)
    last_name = models.CharField('apellidos', max_length=40)
    address = models.CharField('dirección', max_length=50)
    city = models.CharField('ciudad', max_length=20)
    email = models.EmailField('correo', blank=True, null=True)
    sex = models.CharField(
        'sexo',
        max_length=2,
        choices=(('F', 'Femenino'), ('M', 'Masculino')),
        default="F")
    telephone_number = models.IntegerField('teléfono', default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _("Estudiante")
        verbose_name_plural = _("Estudiantes")


class Secretary(models.Model):
    CIS = models.IntegerField(
        'carnet de identidad', default=0, primary_key=True)
    first_name = models.CharField('nombre', max_length=30)
    last_name = models.CharField('apellidos', max_length=40)
    telephone_number = models.IntegerField('número de teléfono', default=0)
    work_zone = models.CharField('zona de trabajo', max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _("Secretaria")
        verbose_name_plural = _("Secretarias")


class ClassRoom(models.Model):
    IdC = models.IntegerField('id del aula', default=0, primary_key=True)
    zone = models.CharField('zona', max_length=30)
    capacity = models.IntegerField('capacidad', default=0)

    def __str__(self):
        return str(self.IdC)

    class Meta:
        verbose_name = _("Aula")
        verbose_name_plural = _("Aulas")


class Career(models.Model):
    name = models.CharField('nombre', max_length=30)
    career = models.IntegerField('plazas', default=0)
    kind = models.CharField(
        'tipo',
        max_length=30,
        choices=(('CPE', 'Curso por Encuentros'), ('EaD',
                                                   'Educación a Distancia')))

    def __str__(self):
        return f'{self.name} ({self.kind})'

    class Meta:
        verbose_name = _("Carrera")
        verbose_name_plural = _("Carreras")


class TitleValidation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='estudiante')
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, verbose_name='aula')
    date = models.DateField('día')
    hora = models.TimeField('hora')

    def __str__(self):
        return str(self.student) + " " + str(self.classroom)

    class Meta:
        verbose_name = _("Validación")
        verbose_name_plural = _("Validaciones")


class ValidatedStudent(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='estudiante')
    grade = models.IntegerField('nota', default=0)
    secretary = models.ForeignKey(
        Secretary, on_delete=models.CASCADE, verbose_name='secretaria')

    def __str__(self):
        return str(self.student) + " " + str(self.grade)

    class Meta:
        verbose_name = _("Estudiante Validado")
        verbose_name_plural = _("Estudiantes Validados")


class ExamLocation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='estudiante')
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, verbose_name='aula')

    def __str__(self):
        return str(self.student)

    class Meta:
        verbose_name = _("Lugar del Examen")
        verbose_name_plural = _("Lugares de los Examenes")


class Claim(models.Model):  #Reclamaciones
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='estudiante')
    new_grade = models.IntegerField(verbose_name='nueva nota', default=0)

    def __str__(self):
        return str(self.student) + " " + str(self.new_grade)

    class Meta:
        verbose_name = _("Reclamación")
        verbose_name_plural = _("Reclamaciones")


class ApprovedStudent(models.Model):  # pasar el nombre a ingles
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='estudiante')
    career = models.ForeignKey(
        Career, on_delete=models.CASCADE, verbose_name='carrera')

    def __str__(self):
        return str(self.student) + " " + str(self.career)

    class Meta:
        verbose_name = _("Estudiante Aprobado")
        verbose_name_plural = _("Estudiantes Aprobados")