from getgems import checker,vars
import requests
from threading import Thread
import schedule
import time



def GGuns():
    r = requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.g_guns,'G-Guns'))


def MetaForest():
    requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.MetaForest_Bunnies,'MetaForest_Bunnies'))


def TonDiamonds():
    requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.TON_Diamonds,'TON Diamonds'))

def Tonlanders():
    requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.Tonlanders_Sheeps,'Tonlanders - Sheeps'))


def TonFrogs():
    requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(vars.Ton_Frogs,'Ton Frogs'))

def CheckErr():
    r = requests.post('https://api.getgems.io/graphql')
    print(r.status_code)
    if (r.status_code == 502) or (r.status_code != 200):
        raise Exception('We are fucked!')

if __name__ == '__main__':
    schedule.every(10).seconds.do(GGuns)
    schedule.every(10).seconds.do(MetaForest)
    schedule.every(10).seconds.do(TonDiamonds)
    schedule.every(10).seconds.do(Tonlanders)
    schedule.every(10).seconds.do(TonFrogs)
    schedule.every(60).seconds.do(CheckErr)

    while True:
        schedule.run_pending()
        time.sleep(1)
