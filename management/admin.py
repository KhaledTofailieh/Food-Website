from django.contrib import admin
from .models import UserExperienceStrategy, MarketingStrategy

# Register your models here.

admin.site.register(MarketingStrategy)
admin.site.register(UserExperienceStrategy)
