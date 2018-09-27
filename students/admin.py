from django.contrib import admin
from students.models import Student, Career, ClassRoom, Secretary

class StudentAdmin(admin.ModelAdmin):
    "Shows what fields to display in the admin site"
    list_display = ('first_name', 'last_name', 'email')
    # Fields to use to search
    search_fields = ('first_name', 'last_name')
    # Possible filter options
    list_filter = ('last_name', 'ci')
    # Order of the students
    ordering = ('first_name', 'last_name')
    # Fields available to change
    #fields  = ('first_name', 'last_name', 'email')

admin.site.register(Student, StudentAdmin)
admin.site.register(Career)
admin.site.register(ClassRoom)
admin.site.register(Secretary)
admin.site.site_header = 'Administrator Site'