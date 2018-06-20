from decimal import *


class Order:
    def __init__(self, price, volume):
        self.price = string_to_decimal(price)
        self.volume = string_to_decimal(volume)

    def getPrice(self):
        return self.price

    def getVolume(self):
        return self.volume


def string_to_decimal(num_string):
    eight_digit_precision = round(Decimal(float(num_string)), 8)
    return eight_digit_precision