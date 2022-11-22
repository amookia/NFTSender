from getgems import checker,vars
import requests
from threading import Thread
import schedule
import time
from getgems.history import historyCollectionNftItems
from getgems.checker import getNftByAddress

def GGuns():
    addresses = historyCollectionNftItems('EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb')
    count = 0
    arr = []
    for item in addresses:
        if count < 5:
            arr.append(getNftByAddress(item,'G-Guns'))
        count +=1
    print(arr)
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))
  

def MetaForest():
    addresses = historyCollectionNftItems('EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6')
    count = 0
    arr = []
    for item in addresses:
        if count < 5:
            arr.append(getNftByAddress(item,'MetaForest_Bunnies'))
        count +=1
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))
    

def TonDiamonds():
    addresses = historyCollectionNftItems('EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir')
    count = 0
    arr = []
    for item in addresses:
        if count < 5:
            arr.append(getNftByAddress(item,'TON Diamonds'))
        count +=1
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))


def Tonlanders():
    addresses = historyCollectionNftItems('EQDi0t0R8yjV1Yu8lWHkDawz2xihHqsGB61-bQVf7EQ8SteO')
    count = 0
    arr = []
    for item in addresses:
        if count < 5:
            arr.append(getNftByAddress(item,'Tonlanders - Sheeps'))
        count +=1
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))
   

def TonFrogs():
    addresses = historyCollectionNftItems('EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6')
    count = 0
    arr = []
    for item in addresses:
        if count < 5:
            arr.append(getNftByAddress(item,'Ton Frogs'))
        count +=1
    requests.post('https://tomantoncoin.com/nft/connect.php',json=(arr))


def CheckErr():
    r = requests.post('https://api.getgems.io/graphql')
    print(r.status_code)
    if (r.status_code == 502) or (r.status_code != 200):
        raise Exception('We are fucked!')

if __name__ == '__main__':
    schedule.every(5).minutes.do(GGuns)
    schedule.every(5).minutes.do(MetaForest)
    schedule.every(5).minutes.do(TonDiamonds)
    schedule.every(5).minutes.do(Tonlanders)
    schedule.every(5).minutes.do(TonFrogs)
    schedule.every(5).minutes.do(CheckErr)

    while True:
        schedule.run_pending()
        time.sleep(1)
