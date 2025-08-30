from django.db import models

class Company(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=200)
    scripcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.symbol} - {self.company_name}"