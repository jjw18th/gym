from django.contrib import admin
from login.models import userlogin
from login.models import Userdetail
from login.models import Trainer
from login.models import Package
admin.site.register(Userdetail)
admin.site.register(userlogin)
admin.site.register(Trainer)
admin.site.register(Package)
