from django.contrib.auth.models import User
from django.db import models
from companies.models import Company

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companies = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Watchlist"