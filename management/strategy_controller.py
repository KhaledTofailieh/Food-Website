from .models import UserExperienceStrategy, MarketingStrategy
from graduation_website import cache


def change_marketing_strategy(new_strategy_key):
    new_strategy = MarketingStrategy.objects.get(key=new_strategy_key)
    new_strategy.isActive = True
    new_strategy.save()
    try:
        cache.ACTIVE_MARKETING_STRATEGY.isActive = False
        cache.ACTIVE_MARKETING_STRATEGY.save()
    except Exception as ex:
        print('Exception:', ex)
    cache.ACTIVE_MARKETING_STRATEGY = new_strategy


def change_application_strategy(new_strategy_key):

    new_strategy = UserExperienceStrategy.objects.get(key=new_strategy_key)
    new_strategy.isActive = True
    new_strategy.save()
    try:
        cache.ACTIVE_APPLICATION_STRATEGY.isActive = False
        cache.ACTIVE_APPLICATION_STRATEGY.save()
    except Exception as ex:
        print('Exception:', ex)
    cache.ACTIVE_APPLICATION_STRATEGY = new_strategy
