from django.db import models

# Create your models here.

class Login(models.Model):
    user = models.CharField(("User Name"), max_length=50)
    password = models.CharField(("Password"), max_length=50)

    

    class Meta:
        verbose_name = ("Login")
        verbose_name_plural = ("Logins")

    def __str__(self):
        return self.user



