from django.contrib import admin
from .models import User, Organisation, Schedule, UserShift

# Register your models here.
admin.site.register(User)
admin.site.register(Organisation)
admin.site.register(Schedule)
admin.site.register(UserShift)