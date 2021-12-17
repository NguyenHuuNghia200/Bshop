from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    isadmin=models.BooleanField(null=False)
    password = models.CharField(max_length=500)
    def register(self):
        self.save()

    def __str__(self):
        return self.email

    def isExists(self):

        if Customer.objects.filter(email = self.email):
            return True

        return  False