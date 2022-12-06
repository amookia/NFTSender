from getgems import vars
from getgems.checker import nftSearch

from getgems.history import historyCollectionNftItems
from getgems.checker import getNftByAddress


# addresses = historyCollectionNftItems('EQDahyr_gPkHBPbhyrvjoHGVFGGj8vXXtL7w14AV3S2JvpTF')
# for item in addresses:
#     print(item)
#     print(getNftByAddress(item))
#     print('----------------')


#Get history -> historyCollectionNftItems
#Get collect -> nftSearch
addresses = historyCollectionNftItems('EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb')
items = nftSearch(vars.g_guns,"")
for item in items:
    address = item['address']
    if address in addresses:
        print(address)
