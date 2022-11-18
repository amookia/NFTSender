from getgems import checker,vars
import requests
from threading import Thread
import schedule
import time
from getgems.history import historyCollectionNftItems
from getgems.checker import getNftByAddress

def GGuns():
  addresses = historyCollectionNftItems('EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb')
  for item in addresses:
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(getNftByAddress(item,'G-Guns')))

def MetaForest():
    addresses = historyCollectionNftItems('EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6')
    for item in addresses:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=(getNftByAddress(item,'MetaForest_Bunnies')))

def TonDiamonds():
    addresses = historyCollectionNftItems('EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir')
    for item in addresses:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=(getNftByAddress(item,'TON Diamonds')))

def Tonlanders():
    addresses = historyCollectionNftItems('EQDi0t0R8yjV1Yu8lWHkDawz2xihHqsGB61-bQVf7EQ8SteO')
    for item in addresses:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=(getNftByAddress(item,'Tonlanders - Sheeps')))

def TonFrogs():
    addresses = historyCollectionNftItems('EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6')
    for item in addresses:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=(getNftByAddress(item,'Ton Frogs')))

def CheckErr():
    r = requests.post('https://api.getgems.io/graphql')
    print(r.status_code)
    if (r.status_code == 502) or (r.status_code != 200):
        raise Exception('We are fucked!')

if __name__ == '__main__':
    schedule.every(15).minutes.do(GGuns)
    schedule.every(15).minutes.do(MetaForest)
    schedule.every(15).minutes.do(TonDiamonds)
    schedule.every(15).minutes.do(Tonlanders)
    schedule.every(15).minutes.do(TonFrogs)
    schedule.every(15).minutes.do(CheckErr)

    while True:
        schedule.run_pending()
        time.sleep(1)
