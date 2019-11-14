import os
from web3 import Web3
from constants import WEB_3_HTTP_URL

def get_w3():
    provider = Web3.HTTPProvider(WEB_3_HTTP_URL)
    w3 = Web3(provider)
    w3.eth.defaultAccount = os.environ.get('public_key')
    # we don't need to sniff the provider, we know its POA

    return w3

def set_gas_prices(w3, args):
    est = args[0].estimateGas()
    args[1]['gas'] = max(args[1]['gas'], est)
    # gas_price should have been handled by computable.py by now
    if not args[1]['gasPrice']:
        raise Exception('Gas price not set')
