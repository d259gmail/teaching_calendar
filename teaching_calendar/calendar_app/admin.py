from django.contrib import admin
from calendar_app.models import Subject, Lesson


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)
