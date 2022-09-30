from getgems import checker,vars
import requests
from threading import Thread
import time


def sendToApi(var):
    try:
        requests.post('http://ashams.tk/nftchannel/connect.php',json=checker.nftSearch(var))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        Thread(sendToApi(vars.g_guns)).start()
        time.sleep(2)