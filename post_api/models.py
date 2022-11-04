from django.db import models

class ArithmeticQueryModel(models.Model):
    operation_type = models.CharField(max_length=15)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"{self.x} {self.operation_type} {self.y}"

