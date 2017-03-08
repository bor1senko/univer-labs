from django.contrib import admin
from models import *

class StudentAdmin(admin.TabularInline):
    model = Student
    extra = 1
    fields = ('last_name', 'first_name', 'third_name')

class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentAdmin]

class RatingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'complid')

admin.site.register(Teacher)
admin.site.register(Faculty)
admin.site.register(Specialty)
admin.site.register(Group, GroupAdmin)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Rating, RatingAdmin)
