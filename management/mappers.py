from . import strategy_controller
from  . import statistics_controller
update_strategy = {
    'market': strategy_controller.change_marketing_strategy,
    'app': strategy_controller.change_application_strategy,
}

update_charts = {
    'sales': statistics_controller.get_sales_per_month,
    'rests': statistics_controller.get_most_popular_rests
}
