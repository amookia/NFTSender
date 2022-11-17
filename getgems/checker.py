import string
from python_graphql_client import GraphqlClient



def nftSearch(variables : string,collectionName : string) -> dict :
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
            
        }
        cursor
        
        }
        info {
        hasNextPage
        
        }
        
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
            
        }
        
        }
        ... on NftContentLottie {
        lottie
        fallbackImage: image {
            sized(width: 500, height: 500)
            
        }
        
        }
        ... on NftContentVideo {
        baseUrl
        sized(width: 500, height: 500)
        preview(width: 250, height: 250)
        
        }
        
    }
    address
    owner {
        wallet
        
    }
    ownerAddress
    collection {
        name
        address
        isRarityValid
        isVerified
        hasRarityAttributes
        isRarityEnabled
    }
    sale {
        ... on NftSaleFixPrice {
        fullPrice
        nftOwnerAddress
        }
        ... on NftSaleAuction {
        minBid
        maxBid
        lastBidAmount
        finishAt
        end
        
        }
        ... on NftSaleFixPriceDisintar {
        fullPrice
        nftOwnerAddress
        
        }
        
    }
    attributes {
        traitType
        value
    }
    reactionCounters {
        likes
        
    }
    rarityRank
    
    }
    """

    data = client.execute(query=query, variables=variables)
    edges = data['data']['historyCollectionNftItems']['items']
    datas = list()
    for i in edges:
        i = i['node']
        name = i['name']
        try:
            image = i['previewImage']['image']['sized'] if 'image' in i['previewImage'] else i['previewImage']['fallbackImage']['sized']
        except:
            image = i['previewImage']['sized']
        ownerAdress = i['ownerAddress']
        address = i['address']
        url = f'https://getgems.io/collection/{ownerAdress}/{address}'
        rarityAtrrs = i ['collection']['hasRarityAttributes']
        price = 0
        attrs = None
        attrs = i['attributes']
        if 'sale' in i :
            sale = i['sale']

            if (sale is not None) and (('price' in sale) or 'fullPrice') : price = i['sale']['fullPrice']
            elif (sale is not None) and ('maxBid' in sale) :
                maxBid = i['sale']['maxBid']
                minBid = i['sale']['minBid']
                price = maxBid if maxBid is not None else minBid
            if int(price) != 0 : price = int(price) / 1000000000
        emoji = False
        for val in attrs:
            if val['traitType'] == 'Elements':
                emoji = True
        datas.append({'collectionName':collectionName,'emoji':emoji,'name':name,'image':image,'ownerAddress':ownerAdress,
        'address':address,'url':url,'price':price,'attributes':attrs}) #change price later
    return datas


def getNftByAddress(address : str , collectionName : str):
  client = GraphqlClient(endpoint="https://api.getgems.io/graphql")
  query = """
  query getNftByAddress($address: String!) {
  nft: alphaNftItemByAddress(address: $address) {
    ...nftItem
    snippet: content {
      ... on NftContentImage {
        image {
          sized(width: 300, height: 300, format: "jpg")
          
        }
        
      }
      ... on NftContentLottie {
        lottie: image {
          sized(width: 300, height: 300, format: "jpg")
          
        }
        
      }
      ... on NftContentVideo {
        video: preview(width: 300, height: 300)
        
      }
      
    }
    
  }
}

fragment nftItem on NftItem {
  name
  description
  address
  ownerAddress
  kind
  sale {
    ... on NftSaleFixPrice {
      address
      fullPrice
      marketplaceFee
      marketplaceFeeAddress
      nftOwnerAddress
      royaltyAddress
      royaltyAmount
      
    }
    ... on NftSaleAuction {
      address
      nftOwnerAddress
      marketplaceFeeAddress
      marketplaceFeePercent
      royaltyAddress
      royaltyPercent
      minBid
      maxBid
      minStep
      minNextBid
      end
      finishAt
      lastBidAmount
      lastBidAddress
      lastBidUser {
        id
        wallet
        avatar
        name
        
      }
      lastBidAt
      version
      
    }
    ... on NftSaleFixPriceDisintar {
      address
      fullPrice
      marketplaceFee
      marketplaceFeeAddress
      nftOwnerAddress
      royaltyAddress
      royaltyAmount
      
    }
    ... on TelemintAuction {
      telemintLastBidAmount: lastBidAmount
      telemintLastBidAddress: lastBidAddress
      telemintLastBidAt: lastBidAt
      telemintFinishAt: finishAt
      telemintNextBidAmount: nextBidAmount
      telemintLastBidUser: lastBidUser {
        name
        wallet
        avatar
        
      }
      
    }
    
  }
  owner {
    name
    avatar
    wallet
    
  }
  index
  metadataSourceType
  content {
    ... on NftContentImage {
      image {
        sized(width: 1000, height: 0)
        baseUrl
        hasAnimation
        animation(width: 500, height: 500)
        layout
        
      }
      
    }
    ... on NftContentLottie {
      lottie
      fallbackImage: image {
        sized(width: 1000, height: 0)
        baseUrl
        
      }
      
    }
    ... on NftContentVideo {
      baseUrl
      sized(width: 500, height: 500)
      preview(width: 250, height: 250)
      
    }
    
  }
  collection {
    name
    address
    image {
      image {
        baseUrl
        sized(width: 100, height: 100, format: "collection-avatar")
        
      }
      
    }
    isVerified
    isRarityValid
    hasRarityAttributes
    isRarityEnabled
    approximateItemsCount
    
  }
  attributes {
    traitType
    value
    
  }
  reactionCounters {
    likes
    
  }
  isApproved
  priority
  isBlocked
  rarityRank
  rarityAttributes {
    traitType
    value
    maxShapeCount
    rarityPercent
    
  }
  maxOffer {
    offerAddress
    fullPrice
    finishAt
    
  }
  isRevealable
  
}
  """
  varss = {"address": address}
  data = client.execute(query=query, variables=varss)
  nft = data['data']['nft']
  name = collectionName #nft['name']
  address = nft['address']
  ownerAddress = nft['ownerAddress']
  price = nft['sale']['fullPrice'] if nft['sale'] is not None else None
  content = nft['content']
  if ('fallbackImage' in content ) or ('image' in content):
    image = content['fallbackImage']['baseUrl'] if 'fallbackImage' in content else content['image']['baseUrl']
  else:
    image = content['baseUrl']
  attributes = nft['attributes']
  emoji = False
  for val in attributes:
    if val['traitType'] == 'Elements':
        emoji = True
  url = f'https://getgems.io/collection/{ownerAddress}/{address}'
  datas = {'name':name,'emoji':emoji,'name':name,'image':image,'ownerAddress':ownerAddress,'address':address,'url':url,'price':price,'attributes':attributes}
  return datas