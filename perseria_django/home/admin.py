from django.contrib import admin
from home.models import Mechanic, BreakdownCover, Vehicle, Job, Cover

admin.site.register(Mechanic)
admin.site.register(BreakdownCover)
admin.site.register(Vehicle)
admin.site.register(Job)
admin.site.register(Cover)