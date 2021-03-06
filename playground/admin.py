from django.contrib import admin

from .models import Student, StudentInfo, Publisher, Article, Shop, Category

admin.site.register(Student)
# admin.site.register(StudentInfo)
admin.site.register(Publisher)
admin.site.register(Article)
admin.site.register(Shop)
admin.site.register(Category)


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pass_id', 'email', 'student')
