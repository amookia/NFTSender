from flask import (Blueprint, jsonify, request)
from getgems.checker import nftSearch

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('test')
def test():
    return jsonify({'test':'test'})

@api.route('nftSearch',methods=['POST'])
def nftSearchRoute():
    x = request.json
    result = nftSearch(x)
    return jsonify(result)