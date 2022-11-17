# from getgems import vars
#from getgems.checker import nftSearch


# x = nftSearch(vars.testG,"")
# print(x)
from getgems.history import historyCollectionNftItems
from getgems.checker import getNftByAddress


addresses = historyCollectionNftItems('EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb')
for item in addresses:
    print(item)
    getNftByAddress(item)
    print('----------------')