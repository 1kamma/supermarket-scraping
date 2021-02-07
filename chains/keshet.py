from chains.cerberus_web_client import CerberusWebClient
from supermarket_chain import SupermarketChain


class Keshet(CerberusWebClient, SupermarketChain):
    _date_hour_format = '%Y-%m-%d %H:%M:%S'
