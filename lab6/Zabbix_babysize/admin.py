from django.contrib import admin
#from .models import Zabbix_babysize
from .models import ServerCategory
from .models import Server

#admin.site.register(Zabbix_babysize)
# Register your models here.
admin.site.register(ServerCategory)
admin.site.register(Server)
