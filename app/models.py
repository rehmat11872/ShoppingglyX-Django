from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
STATE_CHOICE = (
    ("Lahore", "Lahore"),
    ("Karachi", "Karachi"),
    ("Sahiwal", "Sahiwal"),
    ("Multan", "Multan"),
    ("Faisalabad", "Faisalabad"),
    ("Pakpattan", "Pakpattan"),
    ("Islamabad", "Islamabad"),
    ("Patoki", "Patoki"),
    ("Jang", "Jang"),
    ("Murree", "Murree"),
    ("Okara", "Okara"),
    ("Arif Wala", "Arif Wala"),
    ("Dj khan", "DJ khan"),
    ("Sialkot", "Sialkot"),
    ("MianWali", "MianWali"),
    ("Kasoor", "Kasoor"),
    ("Peshawar", "Peshawar"),
    ("Quetta", "Quetta"),
    ("Sargodha", "Sargodha"),
    ("Rawalpindi", "Rawalpindi"),
    ("Gujranwala", "Gujranwala"),

)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)

    def __str___(self):
        return str(self.id)



