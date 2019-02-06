from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    CI = models.BigIntegerField(default=0, primary_key=True)
    first_name = models.CharField('nombre', max_length=30)
    last_name = models.CharField('apellidos', max_length=40)
    address = models.CharField('dirección', max_length=200)
    city = models.CharField('ciudad', max_length=20)
    email = models.EmailField('correo', blank=True, null=True)
    sex = models.CharField(
        'sexo',
        max_length=2,
        choices=(('F', 'Femenino'), ('M', 'Masculino')),
        default="F")
    tel = models.IntegerField('teléfono', default=0, blank=True) 
    town = models.CharField('municipio', max_length=50, default='Playa')
    color = models.CharField(
        'color de piel',
        max_length=1,
        choices=(('1', 'Negro'), ('2', 'Blanco'), ('3', 'Mestizo')),
        default='2'
    )
    procedence = models.CharField(
        'procedencia escolar',
        max_length=20,
        choices=(('1', 'IPU'), ('2', 'Politecnico'), ('3', 'FOC'), ('4', 'Otro')),
        default='1'
    )
    ocupation = models.CharField(
        'ocupacion',
        max_length=20,
        choices=(('1', 'Dirigente'),
                ('2', 'Profesional'),
                ('3', 'Tecnico'),
                ('4', 'Administrativo'),
                ('5', 'Trabajador de los servicios'),
                ('6', 'Obrero'),
                ('7', 'Campesino'),
                ('8', 'Ama de casa'),
                ('9', 'Otra situación')),
        default='3'
    )
    workSec = models.CharField(
        'sector laboral',
        max_length=20,
        choices=(('1', 'Estatal'), ('2', 'Privado'), ('3', 'Cooperativo'), 
                ('4', 'Mixto o Extranjero')),
        default='1'
    )
    vinculation = models.BooleanField('vinculación con la carrera', default=True)
    #TODO: Faltan carreras

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
        verbose_name_plural = _("Lugares del Examen")


class Claim(models.Model):  #Reclamaciones
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='estudiante')
    new_grade = models.IntegerField('nueva nota', default=0)
    
    def __str__(self):
        return str(self.student) + " " + str(self.new_grade)

    class Meta:
        verbose_name = _("Reclamación")
        verbose_name_plural = _("Reclamaciones")


class ApprovedStudent(models.Model): 
    student = models.ForeignKey(
        Student, models.CASCADE, verbose_name='estudiante')
    career = models.ForeignKey(
        Career, models.CASCADE, verbose_name='carrera')
    
    def __str__(self):
        return str(self.student) + " " + str(self.career)

    class Meta:
        verbose_name = _("Estudiante Aprobado")
        verbose_name_plural = _("Estudiantes Aprobados")


class Inscription(models.Model):
    date_start = models.DateField('fecha de inicio')
    date_end = models.DateField('fecha de final')
    
    def __str__(self):
        return 'Inicio de inscripción: ' + str(self.date_start) + ', final: ' + str(self.date_end)

    class Meta:
        verbose_name = _("Inscripción")
        verbose_name_plural = _("Inscripciones")


class Registration(models.Model):
    date_start = models.DateField('fecha inicio')
    date_end = models.DateField('fecha final')
    
    def __str__(self):
        return 'Matrícula inicio: ' + str(self.date_start)  + ', final ' + str(self.date_end)

    class Meta:
        verbose_name = _("Matrícula")
        verbose_name_plural = _("Matrículas")

class Turn(models.Model):
    date = models.DateField('día')
    time = models.TimeField('time')
    secretary = models.IntegerField(_("secretaria"))
    
    def __str__(self):
        return str(self.date) + ' a las ' + str(self.time)

    class Meta:
        verbose_name = _('Turno')
        verbose_name_plural = _('Turnos')

class MakeTurns(models.Model):
    start_day = models.DateField('día de inicio')
    end_day = models.DateField('día final')
    secretary_amount = models.IntegerField('cantidad de secretarias')
    start_time = models.TimeField('horario inicial')
    end_time = models.TimeField('horario final')

    def __str__(self):
        return 'Turno: empieza ' + str(self.start_day) + ' termina ' + str(self.end_day) 
    

    class Meta:
        verbose_name = _('Turno Horario')
        verbose_name_plural = _('Turnos Horarios')

class AssignTurn(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE, verbose_name='turno')
    secretary = models.ForeignKey(Secretary, on_delete=models.CASCADE, verbose_name='secretaria')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='estudiante')
    
    def __str__(self):
        return 'Secretaria: ' + str(self.secretary) + ' el ' + str(self.turn)  + ' a ' + str(self.student)
    
    class Meta:
        verbose_name = _('Turno Asignado')
        verbose_name_plural = _('Turnos Asignados')