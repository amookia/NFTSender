from getgems import checker,vars
import requests
from threading import Thread
import schedule
import time
from getgems.history import historyCollectionNftItems
from getgems.checker import getNftByAddress
from getgems.checker import nftSearch

def GGuns():
    arr = list()
    addresses = historyCollectionNftItems('EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb')
    items = nftSearch(vars.g_guns,"G-Guns")
    for item in items:
        address = item['address']
        if address in addresses:
            arr.append(item)
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))
  

def MetaForest():
    arr = list()
    addresses = historyCollectionNftItems('EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6')
    items = nftSearch(vars.MetaForest_Bunnies,"MetaForest Bunnies")
    for item in items:
        address = item['address']
        if address in addresses:
            arr.append(item)
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))
    

def TonDiamonds():
    arr = list()
    addresses = historyCollectionNftItems('EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir')
    print(addresses)
    items = nftSearch(vars.TON_Diamonds,"Ton Diamonds")
    for item in items:
        address = item['address']
        if address in addresses:
            arr.append(item)
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))


def Tonlanders():
    arr = list()
    addresses = historyCollectionNftItems('EQDi0t0R8yjV1Yu8lWHkDawz2xihHqsGB61-bQVf7EQ8SteO')
    print(addresses)
    items = nftSearch(vars.Tonlanders_Sheeps,"Tonlanders Sheeps")
    for item in items:
        address = item['address']
        if address in addresses:
            arr.append(item)
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))
   

def TonFrogs():
    arr = list()
    addresses = historyCollectionNftItems('EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6')
    items = nftSearch(vars.Ton_Frogs,"Ton Frogs")
    for item in items:
        address = item['address']
        if address in addresses:
            arr.append(item)
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))


def CheckErr():
    r = requests.post('https://api.getgems.io/graphql')
    print(r.status_code)
    if (r.status_code == 502) or (r.status_code != 200):
        raise Exception('We are fucked!')

if __name__ == '__main__':
    schedule.every(10).minutes.do(GGuns)
    schedule.every(12).minutes.do(MetaForest)
    schedule.every(14).minutes.do(TonDiamonds)
    schedule.every(16).minutes.do(Tonlanders)
    schedule.every(18).minutes.do(TonFrogs)
    schedule.every(10).minutes.do(CheckErr)

    while True:
        schedule.run_pending()
        time.sleep(1)
