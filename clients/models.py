from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    client_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    project_name = models.CharField(max_length=150)
    project_deadline = models.DateField()
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.client_id} - {self.name}"
