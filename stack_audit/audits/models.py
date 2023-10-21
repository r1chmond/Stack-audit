from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Evaluation(models.Model):
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    response = models.TextField()

class SmartContract(models.Model):
    contract_address = models.TextField()
    contract_name = models.TextField()
    evalutation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return f"SmartContract({self.contract_name}, {self.contract_address})"


