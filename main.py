from arbitrage import Arbitrage
from decimal import *

arbitrageObj = Arbitrage()


def string_to_decimal(num_string):
    eight_digit_precision = round(Decimal(float(num_string)), 8)
    return eight_digit_precision


total = string_to_decimal(0)

poloAvailableBalanceA = arbitrageObj.polo_client.returnAvailableAccountBalances('string sample')['string sample']['string sample']
poloAvailableBalanceB = arbitrageObj.polo_client.returnAvailableAccountBalances('string sample')['string sample']['string sample']

binBalancesList = arbitrageObj.binance_client.get_account()['string sample']
binAvailabelBalanceA = (next(x for x in binBalancesList if x['string sample'] == 'string sample'))['string sample']
binAvailabelBalanceB = (next(x for x in binBalancesList if x['string sample'] == 'string sample'))['string sample']

while True:
    try:
        result = arbitrageObj.arbitrageStrategies()
        if result is not None:
            total = total+result
    except Exception as e:
        poloAvailableA = arbitrageObj.polo_client.returnAvailableAccountBalances('string sample')['string sample']['string sample']
        poloAvailableA = arbitrageObj.polo_client.returnAvailableAccountBalances('string sample')['string sample']['string sample']
        binBalancesList = arbitrageObj.binance_client.get_account()['string sample']
        binAvailabelA = (next(x for x in binBalancesList if x['string sample'] == 'string sample'))['string sample']
        binAvailabelB = (next(x for x in binBalancesList if x['string sample'] == 'string sample'))['string sample']
        exit(0)