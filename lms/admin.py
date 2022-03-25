from django.contrib import admin

# Register your models here.
from lms.models import Group, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = (LessonInline, )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')