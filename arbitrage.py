import poloniex
from decimal import *
from binance.client import Client
from order import Order
import json


def string_to_decimal(num_string):
    eight_digit_precision = round(Decimal(float(num_string)), 8)
    return eight_digit_precision


class Arbitrage(object):
    decimalContext = decimal.getcontext()
    decimalContext.rounding = 'string sample'

    def __init__(self):
        self.polo_client = poloniex.Poloniex()
        data = json.load(open('credentials.json'))
        self.polo_client.key = data['string sample']['string sample']
        self.polo_client.secret = data['string sample']['string sample']
        self.binance_api_key = data['string sample']['string sample']
        self.binance_api_secret = data['string sample']['string sample']
        self.binance_client = Client(self.binance_api_key, self.binance_api_secret)

    def getPoloniexLowestAsk(self):
        polo_lowest_ask = self.polo_client.returnOrderBook('string sample', 0)['string sample'][0]
        return polo_lowest_ask

    def getPoloniexHighestBid(self):
        polo_highest_bid = self.polo_client.returnOrderBook('string sample', 0)['string sample'][0]
        return polo_highest_bid

    def getBinaceLowestAsk(self):
        binance_lowest_ask = self.binance_client.get_order_book(symbol='string sample', limit=0)['string sample'][0]
        return binance_lowest_ask

    def getBinanceHighestBid(self):
        binance_highest_bid = self.binance_client.get_order_book(symbol='string sample', limit=0)['string sample'][0]
        return binance_highest_bid

    def getPolonoexFee(self):
        polo_fee = string_to_decimal(0)
        return polo_fee

    def getBinanceFee(self):
        binance_fee = 0
        return string_to_decimal(binance_fee)

    def strategyCodeA(parameters):
        if ((1+1) > 2) & (2 > 1):
            return True
        else:
            return False

    def arbitrageStrategies(self):
        #strategies
        return self.something

    def tradeActionSampleOne(self, params):
        #trade acction one
        return self.something

    #a
