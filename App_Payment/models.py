from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PaymentInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    house=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    country=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    zip=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    def is_all_filled(self):
        # check all field are fillup or not 
        all_fildes=[f.name for f in self._meta.get_fields()]

        for filds in all_fildes:
            value=getattr(self, filds)
            if value==None or value== "":
                return False
        return True

