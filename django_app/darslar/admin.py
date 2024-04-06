from django.contrib import admin
from .models import User, Category, SubCategory, Lesson
# Register your models here.


admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Lesson)
