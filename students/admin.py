from django.contrib import admin
from students.models import *
from datetime import time, date

class StudentAdmin(admin.ModelAdmin):
    "Shows what fields to display in the admin site"
    list_display = ('first_name', 'last_name', 'email')
    # Fields to use to search
    search_fields = ('first_name', 'last_name')
    # Possible filter options
    list_filter = ('last_name', 'CI')
    # Order of the students
    ordering = ('first_name', 'last_name')
    # Fields available to change
    #fields  = ('first_name', 'last_name', 'email')


class MakeTurnsAdmin(admin.ModelAdmin):
    @staticmethod
    def _get_times(start:time, end:time, duration:int):
        """Obtiene todos los turnos de un día que comienzan en `start` y terminan
        en `end`, teniendo entre ellos la duración especificada en `duration`
        """
        times = []
        current = start
        while current <= end:
            times.append(current)
            try:
                current = time(current.hour, current.minute + duration)
            except ValueError:
                current = time(current.hour + 1, current.minute + duration - 60)
        print(times)
        return times

    @staticmethod
    def _get_next_day(ndate:date):
        """
        Retorna el día siguiente después de la fecha especificada en `ndate`
        """
        try:
            return date(ndate.year, ndate.month, ndate.day + 1)
        except ValueError:
            if ndate.month != 12:
                return date(ndate.year, ndate.month + 1, 1)
            return date(ndate.year+1, 1, 1)

    def save_model(self, request, obj, form, change):
        """
        Función que se llama cuando se salva un nuevo campo.
        """
        days = obj.end_day-obj.start_day
        hours = _get_times(obj.start_time, obj.end_time)
        
        current = obj.start_day
        end = obj.end_day
        while current <= end:
            for time in hours:
                for sec in range(obj.secretary_amount):
                    Turn.objects.create(date=current, time=time,
                                        secretary=sec)
            current = _get_next_day(current)
        super().save_model(request, obj, form, change)

   


class TurnAdmin(admin.ModelAdmin):
    list_filter = ('date', 'time')


admin.site.register(Student, StudentAdmin)
admin.site.register(Career)
admin.site.register(ClassRoom)
admin.site.register(Secretary)
admin.site.register(TitleValidation)
admin.site.register(ValidatedStudent)
admin.site.register(ExamLocation)
admin.site.register(Claim)
admin.site.register(ApprovedStudent)
admin.site.register(Inscription)
admin.site.register(Registration)
admin.site.register(Turn, TurnAdmin)
# admin.site.register(AssignTurn)
admin.site.register(MakeTurns, MakeTurnsAdmin)

admin.site.site_header = 'Sitio de Administración'