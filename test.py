from trading_ig import IGService

class config_ru(object):
    username = "rubentest"
    password = "Stopregarderchien75"
    api_key = "e9802443af7a74ccc0520a6efe6aeb8214aa48fb"
    acc_type = "DEMO"
    acc_number = "Z40TAF"

lscac = [
    ("AirLiquide", "Air Liquide", "model_AirLiquide", "EC.D.AI.CASH.IP")
]

ig_service = IGService(config_ru.username, config_ru.password, config_ru.api_key, config_ru.acc_type,
                       acc_number=config_ru.acc_number)
ig_service.create_session()

for elemento in lscac:


    #print(close_pred, "DOWN")
    ig_service.create_working_order(currency_code='EUR', direction='BUY', epic=elemento[3],
    expiry="-", force_open=False, guaranteed_stop='false',
    level='164', time_in_force='GOOD_TILL_CANCELLED', limit_distance=None, limit_level='167',
    order_type='LIMIT', size='50',  stop_distance=None, good_till_date=None,deal_reference=None,
    stop_level= '162')














