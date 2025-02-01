from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=10)

    def __str__(self):
        return self.role_name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


    def __str__(self):
        return self.name + " - " + self.role.role_name

