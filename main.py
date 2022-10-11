from getgems import checker,vars
import requests
from threading import Thread
import time


def sendToApi(var,c):
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(var,c))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        Thread(sendToApi(vars.g_guns,'G-Guns')).start()
        Thread(sendToApi(vars.MetaForest_Bunnies,'MetaForest_Bunnies')).start()
        Thread(sendToApi(vars.TON_Diamonds,'TON Diamonds')).start()
        Thread(sendToApi(vars.Tonlanders_Sheeps,'Tonlanders - Sheeps')).start()
        Thread(sendToApi(vars.Ton_Frogs,'Ton Frogs')).start()

        time.sleep(15)