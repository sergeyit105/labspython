from django.db import models


# Create your models here.
class ServerCategory(models.Model):
    name = models.CharField(max_length = 100, default='Prodact')

    def __str__(self):
        return self.name

class Server(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField()
    location = models.CharField(max_length = 100)
    category = models.ForeignKey(ServerCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



