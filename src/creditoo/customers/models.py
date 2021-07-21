from django.db import models

# Create your models here.

class City:
    id= models.IntegerField
    name= models.CharField(max_length=150)
    zip_code = models.CharField(max_length=20)
    

class Person(models.Model):
    id = models.IntegerField()
    identification_number = models.IntegerField()
    expedition_date = models.DateField()
    city = models.IntegerField()
    state = models.IntegerField()
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Borrower(Person):
    client_id = models.IntegerField()
