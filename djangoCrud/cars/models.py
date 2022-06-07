from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length = 30)
    class Meta:
        db_table="Brand"
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    price = models.IntegerField()
    class Meta:
        db_table="Car"
        
    def __str__(self):
        return self.name
