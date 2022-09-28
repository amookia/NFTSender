from python_graphql_client import GraphqlClient


client = GraphqlClient(endpoint="https://api.getgems.io/graphql")

# Create the query string and variables required for the request.
query = """
query nftSearch($count: Int!, $cursor: String, $query: String, $sort: String, $attributes: String) {
  alphaNftItemSearch(
    first: $count
    after: $cursor
    query: $query
    sort: $sort
    attributes: $attributes
  ) {
    edges {
      node {
        ...nftPreview
        __typename
      }
      cursor
      __typename
    }
    info {
      hasNextPage
      __typename
    }
    __typename
  }
}

fragment nftPreview on NftItem {
  name
  previewImage: content {
    ... on NftContentImage {
      image {
        baseUrl
        sized(width: 500, height: 500)
        hasAnimation
        animation(width: 500, height: 500)
        preview(width: 250, height: 250)
        __typename
      }
      __typename
    }
    ... on NftContentLottie {
      lottie
      fallbackImage: image {
        sized(width: 500, height: 500)
        __typename
      }
      __typename
    }
    ... on NftContentVideo {
      baseUrl
      sized(width: 500, height: 500)
      preview(width: 250, height: 250)
      __typename
    }
    __typename
  }
  address
  owner {
    wallet
    __typename
  }
  ownerAddress
  collection {
    name
    address
    isRarityValid
    isVerified
    hasRarityAttributes
    isRarityEnabled
    __typename
  }
  sale {
    ... on NftSaleFixPrice {
      fullPrice
      nftOwnerAddress
      __typename
    }
    ... on NftSaleAuction {
      minBid
      maxBid
      lastBidAmount
      finishAt
      end
      __typename
    }
    ... on NftSaleFixPriceDisintar {
      fullPrice
      nftOwnerAddress
      __typename
    }
    __typename
  }
  attributes {
    traitType
    value
    __typename
  }
  reactionCounters {
    likes
    __typename
  }
  rarityRank
  __typename
}
"""
variables = {
  "query": "{\"$and\":[{\"collectionAddress\":\"EQBpOQjo6uIpkH-GqJ1oObqVjyATQEJ1PnIrM_52f3nSE_rb\"}]}",
  "attributes": "[[\"Elements\",[\"Diamond\",null,\"Common\",\"Rare\",\"Gold\"]],[\"Inner Body\",[\"Rare\"]],[\"Outer Body\",[\"Rare\",\"Gold\"]],[\"Type\",[\"G-Pistols\",\"G-Shotguns\"]]]",
  "sort": "[{\"isOnSale\":{\"order\":\"desc\"}},{\"price\":{\"order\":\"asc\"}},{\"index\":{\"order\":\"asc\"}}]",
  "count": 30
}

data = client.execute(query=query, variables=variables)
edges = data['data']['alphaNftItemSearch']['edges']
for i in edges:
    i = i['node']
    name = i['name']
    image = i['previewImage']['image']['sized']
    ownerAdress = i['ownerAddress']
    address = i['address']
    url = f'https://getgems.io/collection/{ownerAdress}/{address}'
    rarityAtrrs = i ['collection']['hasRarityAttributes']
    #attrs = 
    #print(rarityAtrrs)
    print(name)
    print(image)
    print(ownerAdress)
    print(address)
    print(url)
    print('------------')

#G-Guns 
#( 5 elements ) ( rare -> inner body ) ( rare , gold -> outter body ) ( g-shutgun , g-pistol -> type)
#------------------




# {
#   "minBid": "30000000000", -> min price
#   "maxBid": null,
#   "lastBidAmount": "37000000000", -> last price
#   "finishAt": 1664613136,
#   "end": false,
#   "__typename": "NftSaleAuction"
# }
