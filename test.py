# from getgems import vars
#from getgems.checker import nftSearch


# x = nftSearch(vars.testG,"")
# print(x)
from getgems.history import historyCollectionNftItems
from getgems.checker import getNftByAddress


addresses = historyCollectionNftItems('EQDahyr_gPkHBPbhyrvjoHGVFGGj8vXXtL7w14AV3S2JvpTF')
for item in addresses:
    print(item)
    print(getNftByAddress(item))
    print('----------------')