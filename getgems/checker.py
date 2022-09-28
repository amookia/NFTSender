import string
from python_graphql_client import GraphqlClient



def nftSearch(variables : string) -> dict :
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

    data = client.execute(query=query, variables=variables)
    edges = data['data']['alphaNftItemSearch']['edges']
    datas = list()
    for i in edges:
        i = i['node']
        name = i['name']
        image = i['previewImage']['image']['sized']
        ownerAdress = i['ownerAddress']
        address = i['address']
        url = f'https://getgems.io/collection/{ownerAdress}/{address}'
        rarityAtrrs = i ['collection']['hasRarityAttributes']
        price = 0
        datas.append({'name':name,'image':image,'ownerAddress':ownerAdress,
        'address':address,'url':url,'price':price})
    return datas


