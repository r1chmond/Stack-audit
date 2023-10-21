from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Evaluation(models.Model):
    response = models.TextField()

class SmartContract(models.Model):
    contract_address = models.TextField(blank=True)
    contract_name = models.TextField(blank=True)
    evalutation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    source = models.TextField()

    def __str__(self):
        return f"SmartContract({self.contract_name}, {self.contract_address})"


