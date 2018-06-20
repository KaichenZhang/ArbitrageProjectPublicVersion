from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
from binance.websockets import BinanceSocketManager

api_key = 'string sample'
api_secret = 'string sample'
client = Client(api_key, api_secret)

depth = client.get_order_book(symbol='string sample')

order = client.create_test_order(
    symbol='string sample',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=0)


try:
    result = client.withdraw(
        asset='string sample',
        address='<string sample>',
        amount=0)
except BinanceAPIException as e:
    print(e)
except BinanceWithdrawException as e:
    print(e)
else:
    print("string sample")

withdraws = client.get_withdraw_history()
eth_withdraws = client.get_withdraw_history(asset='string sample')
address = client.get_deposit_address(asset='string sample')


def process_message(msg):
    # do something


bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('string sample', process_message)

klines1Min = client.get_historical_klines("string sample", Client.KLINE_INTERVAL_1MINUTE, "string sample")
klines30Min = client.get_historical_klines("string sample", Client.KLINE_INTERVAL_30MINUTE, "string sample", "string sample")
klines1W = client.get_historical_klines("string sample", Client.KLINE_INTERVAL_1WEEK, "string sample")
