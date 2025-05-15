from django.contrib import admin
from .models import Student, EducationProgram, ManagementMember, FellowStudent

# Register your models here.

admin.site.register(Student)
admin.site.register(EducationProgram)
admin.site.register(ManagementMember)
admin.site.register(FellowStudent)

# admin.site.register(AbcModel)
# @admin.register(Abc)
# class AbcAdmin(admin.ModelAdmin):
#     list_display = ['id', 'task', 'a', 'b', 'c', 'current_date']
#     list_editable = ['task', 'a', 'b', 'c']
#     search_fields = ['task', 'a', 'b', 'c']
#     list_filter = ['task', 'a', 'b', 'c']
#     list_per_page = 15
#

