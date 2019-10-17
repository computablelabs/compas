import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from constants import WEB_3_HTTP_URL

def get_w3():
    provider = Web3.HTTPProvider(WEB_3_HTTP_URL)
    w3 = Web3(provider)
    w3.eth.defaultAccount = os.environ.get('public_key')
    if 'skynet' in WEB_3_HTTP_URL:
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    return w3

def set_gas_prices(w3, args):
    est = args[0].estimateGas()
    args[1]['gas'] = max(args[1]['gas'], est)
    args[1]['gasPrice'] = w3.toWei(2, 'gwei')
