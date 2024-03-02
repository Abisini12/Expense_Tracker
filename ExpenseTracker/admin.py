from django.contrib import admin

from .models import Userinfo,reportinfo,productinfo
# Register your models here.

admin.site.register(Userinfo)
admin.site.register(reportinfo)
admin.site.register(productinfo)

