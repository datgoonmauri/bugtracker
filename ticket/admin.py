from django.contrib import admin
from ticket.models import CustomUser, Tickets
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Tickets)

