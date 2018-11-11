# Generated by Django 2.1 on 2018-10-31 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20181009_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Estudiante Aprobado',
                'verbose_name_plural': 'Estudiantes Aprobados',
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(unique_for_year=True, verbose_name='fecha de inicio')),
                ('date_end', models.DateField(verbose_name='fecha de final')),
            ],
            options={
                'verbose_name': 'Inscripción',
                'verbose_name_plural': 'Inscripciones',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='fecha inicio')),
                ('date_end', models.DateField(verbose_name='fecha final')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matrículas',
            },
        ),
        migrations.RemoveField(
            model_name='estudianteaprobado',
            name='career',
        ),
        migrations.RemoveField(
            model_name='estudianteaprobado',
            name='student',
        ),
        migrations.AlterModelOptions(
            name='career',
            options={'verbose_name': 'Carrera', 'verbose_name_plural': 'Carreras'},
        ),
        migrations.AlterModelOptions(
            name='claim',
            options={'verbose_name': 'Reclamación', 'verbose_name_plural': 'Reclamaciones'},
        ),
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'Aula', 'verbose_name_plural': 'Aulas'},
        ),
        migrations.AlterModelOptions(
            name='examlocation',
            options={'verbose_name': 'Lugar del Examen', 'verbose_name_plural': 'Lugares del Examen'},
        ),
        migrations.AlterModelOptions(
            name='secretary',
            options={'verbose_name': 'Secretaria', 'verbose_name_plural': 'Secretarias'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='titlevalidation',
            options={'verbose_name': 'Validación', 'verbose_name_plural': 'Validaciones'},
        ),
        migrations.AlterModelOptions(
            name='validatedstudent',
            options={'verbose_name': 'Estudiante Validado', 'verbose_name_plural': 'Estudiantes Validados'},
        ),
        migrations.AlterField(
            model_name='career',
            name='career',
            field=models.IntegerField(default=0, verbose_name='plazas'),
        ),
        migrations.AlterField(
            model_name='career',
            name='kind',
            field=models.CharField(choices=[('CPE', 'Curso por Encuentros'), ('EaD', 'Educación a Distancia')], max_length=30, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='career',
            name='name',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='new_grade',
            field=models.IntegerField(default=0, verbose_name='nueva nota'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='estudiante'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='IdC',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='id del aula'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='capacity',
            field=models.IntegerField(default=0, verbose_name='capacidad'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='zone',
            field=models.CharField(max_length=30, verbose_name='zona'),
        ),
        migrations.AlterField(
            model_name='examlocation',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.ClassRoom', verbose_name='aula'),
        ),
        migrations.AlterField(
            model_name='examlocation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='estudiante'),
        ),
        migrations.AlterField(
            model_name='secretary',
            name='CIS',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='carnet de identidad'),
        ),
        migrations.AlterField(
            model_name='secretary',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='secretary',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='secretary',
            name='telephone_number',
            field=models.IntegerField(default=0, verbose_name='número de teléfono'),
        ),
        migrations.AlterField(
            model_name='secretary',
            name='work_zone',
            field=models.CharField(max_length=20, verbose_name='zona de trabajo'),
        ),
        migrations.AlterField(
            model_name='titlevalidation',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.ClassRoom', verbose_name='aula'),
        ),
        migrations.AlterField(
            model_name='titlevalidation',
            name='date',
            field=models.DateField(verbose_name='día'),
        ),
        migrations.AlterField(
            model_name='titlevalidation',
            name='hora',
            field=models.TimeField(verbose_name='hora'),
        ),
        migrations.AlterField(
            model_name='titlevalidation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='estudiante'),
        ),
        migrations.AlterField(
            model_name='validatedstudent',
            name='grade',
            field=models.IntegerField(default=0, verbose_name='nota'),
        ),
        migrations.AlterField(
            model_name='validatedstudent',
            name='secretary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Secretary', verbose_name='secretaria'),
        ),
        migrations.AlterField(
            model_name='validatedstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='estudiante'),
        ),
        migrations.DeleteModel(
            name='EstudianteAprobado',
        ),
        migrations.AddField(
            model_name='approvedstudent',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Career', verbose_name='carrera'),
        ),
        migrations.AddField(
            model_name='approvedstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='estudiante'),
        ),
    ]