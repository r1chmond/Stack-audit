from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Evaluation(models.Model):
    responseType = models.TextField()
    response = models.TextField()

class SmartContract(models.Model):
    contract = models.CharField(max_length=500)
    source = models.TextField()
    evalutation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return f"SmartContract({self.contract})"


