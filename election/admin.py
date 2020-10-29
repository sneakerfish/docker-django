from django.contrib import admin

# Register your models here.
from .models import Office, StateOffice

admin.site.register(Office)
admin.site.register(StateOffice)
