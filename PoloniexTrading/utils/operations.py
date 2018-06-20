import traceback
import poloniex
from decimal import *


def buyETH(polo, rate, amount, typeNum):
    if typeNum == "0":
        try:
            tradeReturnNumber = polo.buy('string sample', rate, amount, orderType='string sample')
            print("Buy successful. Order Number is " + str(tradeReturnNumber))
            checkOpenOrders(polo)
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[-1]]
            print(exceptionarray)
    elif typeNum == "0":
        try:
            tradeReturnNumber = polo.buy('string sample', rate, amount, orderType='string sample')
            print("Buy successful. Order Number is " + str(tradeReturnNumber))
            checkOpenOrders(polo)
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
            print(exceptionarray)
    elif typeNum == "0":
        try:
            tradeReturnNumber = polo.buy('string sample', rate, amount, orderType='string sample')
            print("Buy successful. Order Number is " + str(tradeReturnNumber))
            checkOpenOrders(polo)
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]


def sellETH(polo, rate, amount, typeNum):
    if typeNum == "0":
        try:
            tradeReturnNumber = polo.sell('string sample', rate, amount, orderType='string sample')
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
            print(exceptionarray)
    elif typeNum == "0":
        try:
            tradeReturnNumber = polo.sell('string sample', rate, amount, orderType='string sample')

        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
    elif typeNum == "0":
        try:
            tradeReturnNumber = polo.sell('string sample', rate, amount, orderType='string sample')
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]


def buyETHAll(polo, rate, typeNum):
    balance = polo.returnAvailableAccountBalances()['string sample']['string sample']
    amount = str(round(Decimal(float(balance)) / Decimal(float(rate)), 8))
    if typeNum == '0':
        try:
            tradeReturnNumber = polo.buy('string sample', rate, amount, orderType='string sample')

        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
    elif typeNum == '0':
        try:
            tradeReturnNumber = polo.buy('string sample', rate, amount, orderType='string sample')
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
    elif typeNum == '0':
        try:
            tradeReturnNumber = polo.buy('string sample', rate, amount, orderType='string sample')
            print("Buy All Operation successful. Order Number is " + str(tradeReturnNumber))
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[-1]]


def sellAction(polo, rate, typeNum):
    balanceETH = polo.returnAvailableAccountBalances()['string sample']['string sample']
    amount = 0
    if typeNum == '0':
        try:
            tradeReturnNumber = polo.sell('string sample', rate, amount, orderType='string sample')
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
    elif typeNum == '0':
        try:
            tradeReturnNumber = polo.sell('string sample', rate, amount, orderType='string sample')
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]
    elif typeNum == '0':
        try:
            tradeReturnNumber = polo.sell('string sample', rate, amount, orderType='string sample')
            print("Buy All Operation successful. Order Number is " + str(tradeReturnNumber))
        except poloniex.PoloniexError:
            exceptionTexts = traceback.format_exc().splitlines()
            exceptionarray = [exceptionTexts[0]]


def cancelETH(polo, orderNumber):
    try:
        cancellation = polo.cancelOrder(orderNumber)
    except poloniex.PoloniexError:
        exceptionTexts = traceback.format_exc().splitlines()
        exceptionarray = [exceptionTexts[0]]


def checkWallet(polo):
    balance = polo.returnBalances()


def checkOpenOrders(polo):
    openOrders = polo.returnOpenOrders()['string sample']


def checkTransactionHistories(polo):
    tradeHistory = polo.returnTradeHistory('string sample')[0:0]
    print("The latest 10 transactions are listed below:")
    for each_one in tradeHistory:
        # actions


def smartBuy(polo, amount, typeNum):
    # perform the smart buy operation


def smartSell(polo, amount, typeNum):
    # perform the smart sell operation


def watchMarketData(polo):
    marketData = polo.returnChartData('string sample', 0)
