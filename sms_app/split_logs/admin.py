from django.contrib import admin

from .models import FileOriginal, DirOriginal, PublicKey, Organisation, Course, CourseDump, CourseDumpTable

class DirOriginalAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
class FileOriginalAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'lines_total', 'lines_error', 'created', 'updated')
    search_fields = ['name']
    list_filter = ['dir_original']
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'organisation', 'active', 'created', 'updated')
    list_filter = ['organisation']
class CourseDumpAdmin(admin.ModelAdmin):
    list_display = ('course', 'table', 'date', 'is_encypted', 'created', 'updated')
    list_filter = ['course__organisation', 'date', 'is_encypted']
    search_fields = ['course__name']
class CourseDumpTableAdmin(admin.ModelAdmin):
    list_display = ('db_type', 'db_name', 'name', 'primary_key', 'created', 'updated')

admin.site.register(DirOriginal, DirOriginalAdmin)
admin.site.register(FileOriginal, FileOriginalAdmin)
admin.site.register(PublicKey)
admin.site.register(Organisation)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDump, CourseDumpAdmin)
admin.site.register(CourseDumpTable, CourseDumpTableAdmin)
