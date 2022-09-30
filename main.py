from getgems import checker,vars
import requests
from threading import Thread
import time


def sendToApi(var,c):
    try:
        requests.post('http://ashams.tk/nftchannel/connect.php',json=checker.nftSearch(var,c))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        Thread(sendToApi(vars.g_guns,'G-Guns')).start()
        Thread(sendToApi(vars.MetaForest_Bunnies,'MetaForest_Bunnies'))
        time.sleep(5)