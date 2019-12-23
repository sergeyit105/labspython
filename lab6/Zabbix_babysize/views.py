from django.views.generic import CreateView
from django.shortcuts import render
#from .models import Zabbix_babysize
from .models import Server, ServerCategory
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

#class ServerCreateView(CreateView):
#    model = Zabbix_babysize
#    fields = ('id','name', 'time', 'date', 'ntype','email','gtype','group','locate')

def server(request, id):
 server = Server.objects.filter(id=id).values()
 category = ServerCategory.objects.filter(id=list(server)[0]['category_id']).values()
 return render(request, "server.html", context={"server": list(server)[0], "category": list(category)[0]})

def servers(request):
 servers=Server.objects.all()
 return render(request, "servers.html", context={"servers": list(servers)})
