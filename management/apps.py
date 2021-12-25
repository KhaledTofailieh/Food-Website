from django.apps import AppConfig
from graduation_website import cache


class ManagementConfig(AppConfig):
    name = 'management'

    def ready(self):
        from management.models import UserExperienceStrategy, MarketingStrategy

        cache.ACTIVE_MARKETING_STRATEGY = MarketingStrategy.objects.filter(isActive=True).first()
        cache.ACTIVE_APPLICATION_STRATEGY = UserExperienceStrategy.objects.filter(isActive=True).first()
        pass
