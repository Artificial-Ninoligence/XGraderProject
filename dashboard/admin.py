from django.contrib import admin
from .models import Schedule, Module, Assessment

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Module)
admin.site.register(Assessment)