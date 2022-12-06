from python_graphql_client import GraphqlClient

def historyCollectionNftItems(collectionAddress : str):
    client = GraphqlClient(endpoint="https://api.getgems.io/graphql")
    query = """
    query historyCollectionNftItems($collectionAddress: String!, $count: Int!, $cursor: String, $types: [HistoryType!], $maxTime: Int, $minTime: Int) {
  historyCollectionNftItems(
    collectionAddress: $collectionAddress
    first: $count
    after: $cursor
    types: $types
    maxTime: $maxTime
    minTime: $minTime
  ) {
    cursor
    items {
      ...nftHistoryItem
      __typename
    }
    __typename
  }
}

fragment nftHistoryItem on NftItemHistory {
  id
  address
  time
  createdAt
  nft {
    ...transactionNftItem
    __typename
  }
  collectionAddress
  lt
  hash
  typeData {
    __typename
    ... on HistoryTypeMint {
      type
      __typename
    }
    ... on HistoryTypeTransfer {
      type
      oldOwner
      newOwner
      oldOwnerUser {
        ...userDataPreview
        __typename
      }
      newOwnerUser {
        ...userDataPreview
        __typename
      }
      __typename
    }
    ... on HistoryTypeCancelSale {
      type
      owner
      price
      ownerUser {
        ...userDataPreview
        __typename
      }
      __typename
    }
    ... on HistoryTypeSold {
      type
      oldOwner
      newOwner
      oldOwnerUser {
        ...userDataPreview
        __typename
      }
      newOwnerUser {
        ...userDataPreview
        __typename
      }
      price
      __typename
    }
    ... on HistoryTypePutUpForSale {
      type
      owner
      ownerUser {
        ...userDataPreview
        __typename
      }
      price
      __typename
    }
    ... on HistoryTypeCancelAuction {
      type
      historyType
      owner
      ownerUser {
        ...userDataPreview
        __typename
      }
      __typename
    }
    ... on HistoryTypePutUpForAuction {
      type
      historyType
      owner
      ownerUser {
        ...userDataPreview
        __typename
      }
      __typename
    }
  }
  __typename
}

fragment transactionNftItem on NftItem {
  name
  address
  content {
    ... on NftContentImage {
      image {
        sized(width: 56, height: 0)
        __typename
      }
      __typename
    }
    ... on NftContentLottie {
      fallbackImage: image {
        sized(width: 56, height: 0)
        __typename
      }
      __typename
    }
    ... on NftContentVideo {
      preview(width: 56, height: 56)
      __typename
    }
    __typename
  }
  __typename
}

fragment userDataPreview on User {
  id
  avatar
  name
  __typename
}
    """
    varss = {
    "collectionAddress": collectionAddress,
    "count": 40,
    "types": [
    "PutUpForSale"
  ]
}
    data = client.execute(query=query, variables=varss)
    items = data['data']['historyCollectionNftItems']['items']
    datas = list()
    for item in items:
        address = item['address']
        datas.append(address)
    return datas
        