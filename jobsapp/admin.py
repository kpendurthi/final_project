from django.contrib import admin

# Register your models here.
from .models import Employer, Job

# Register your models here.
admin.site.register(Employer)
admin.site.register(Job)