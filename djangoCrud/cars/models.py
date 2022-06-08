from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    price = models.IntegerField()
        
    def __str__(self):
        return self.name
