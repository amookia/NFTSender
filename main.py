from getgems import checker,vars
import requests
from threading import Thread
import time


def sendToApi(var,c):
    try:
        requests.post('https://tomantoncoin.com/nft/connect.php',json=checker.nftSearch(var,c))
    except:
        pass

if __name__ == '__main__':
    while True:
        t1 = Thread(sendToApi(vars.g_guns,'G-Guns'))
        t2 = Thread(sendToApi(vars.MetaForest_Bunnies,'MetaForest_Bunnies'))
        t3 = Thread(sendToApi(vars.TON_Diamonds,'TON Diamonds'))
        t4 = Thread(sendToApi(vars.Tonlanders_Sheeps,'Tonlanders - Sheeps'))
        t5 = Thread(sendToApi(vars.Ton_Frogs,'Ton Frogs'))

        t1.start()
        t1.join()

        t2.start()
        t2.join()

        t3.start()
        t3.join()

        t4.start()
        t4.join()

        t5.start()
        t5.join()

        time.sleep(15)