from django.contrib import admin
from .models import Applicant

# Register your models here.
@admin.register(Applicant)

class Applicantadmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']