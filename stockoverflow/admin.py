from django.contrib import admin
from . models import user, Questions, Answers

admin.site.register(user)
admin.site.register(Questions)
admin.site.register(Answers)
