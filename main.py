from getgems import checker,vars
import requests
from threading import Thread
import schedule
import time



def GGuns():
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.g_guns,'G-Guns'))
    except:
        pass

def MetaForest():
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.MetaForest_Bunnies,'MetaForest_Bunnies'))
    except:
        pass

def TonDiamonds():
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.TON_Diamonds,'TON Diamonds'))
    except:
        pass

def Tonlanders():
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.Tonlanders_Sheeps,'Tonlanders - Sheeps'))
    except:
        pass

def TonFrogs():
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.Ton_Frogs,'Ton Frogs'))
    except:
        pass

if __name__ == '__main__':
    schedule.every(10).seconds.do(GGuns)
    schedule.every(10).seconds.do(MetaForest)
    schedule.every(10).seconds.do(TonDiamonds)
    schedule.every(10).seconds.do(Tonlanders)
    schedule.every(10).seconds.do(TonFrogs)

    while True:
        schedule.run_pending()
        time.sleep(1)
