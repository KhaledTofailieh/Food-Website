from django.db import models


# Create your models here.
class MarketingStrategy(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='', null=True)
    url = models.CharField(max_length=50, default='', null=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserExperienceStrategy(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='', null=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name
