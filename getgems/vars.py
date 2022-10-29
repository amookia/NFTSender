count = 15

g_guns = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": "[[\"Type\",[\"G-Shotguns\",\"G-Pistols\"]]]",
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}
#------------------------

MetaForest_Bunnies = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": None,
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}
#------------------------
TON_Diamonds = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": None,
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}
#------------------------
Tonlanders_Sheeps = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQDi0t0R8yjV1Yu8lWHkDawz2xihHqsGB61-bQVf7EQ8SteO\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": None,
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}
#------------------------
Ton_Frogs = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQDahyr_gPkHBPbhyrvjoHGVFGGj8vXXtL7w14AV3S2JvpTF\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": None,
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}


testG = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb\"}]}",
  "attributes": "[[\"Elements\",[null,\"Common\"]]]",
  "sort": "[{\"isOnSale\":{\"order\":\"desc\"}},{\"price\":{\"order\":\"asc\"}},{\"index\":{\"order\":\"asc\"}}]",
  "count": 1
}