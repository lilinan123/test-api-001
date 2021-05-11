from django.contrib import admin

# Register your models here.
from Myapp.models import *
admin.site.register(DB_tucao) #注册表
admin.site.register(DB_home_href) #注册表
admin.site.register(DB_project)
admin.site.register(DB_apis)
