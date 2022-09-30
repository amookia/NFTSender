count = 15
#G-Guns Collection
#( 5 elements ) ( rare -> inner body ) ( rare , gold -> outter body ) ( g-shutgun , g-pistol -> type)
g_guns = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": "[[\"Elements\",[\"Common\",\"Rare\",\"Gold\",\"Diamond\",null]],[\"Inner Body\",[\"Rare\"]],[\"Outer Body\",[\"Gold\",\"Rare\"]],[\"Type\",[\"G-Shotguns\",\"G-Pistols\"]]]",
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}
#------------------------

MetaForest_Bunnies = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQAu3uEK8pxgAZ29QSYhRtDwmQpqJRbziH24gnud8BDGLRB6\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": "[[\"rarity\",[\"rare\",\"uncommon\",\"common\"]]]",
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}
#------------------------
TON_Diamonds = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir\"},{\"saleType\":\"fix_price\"}]}",
  "attributes": "[[\"Shape\",[\"Diamond\",\"Heart\"]],[\"Size\",[\"Big\",\"Medium\",\"Small\"]]]",
  "sort": "[{\"index\":{\"order\":\"desc\"}}]",
  "count": count
}