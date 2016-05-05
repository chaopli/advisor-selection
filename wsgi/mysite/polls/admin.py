from django.contrib import admin
from .models import Advisor
from .models import Student

admin.site.register(Advisor)
admin.site.register(Student)
