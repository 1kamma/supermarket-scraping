from typing import Dict, List
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from item import Item
from supermarket_chain import SupermarketChain


class CoOp(SupermarketChain):

    promotion_tag_name = 'Sale'
    promotion_update_tag_name = 'PriceUpdateDate'
    date_format = '%Y/%m/%d'
    date_hour_format = '%Y/%m/%d %H:%M:%S'
    item_tag_name = 'Product'

    @property
    def update_date_format(self):
        return CoOp.date_hour_format

    @staticmethod
    def get_download_url(store_id: int, category: SupermarketChain.XMLFilesCategory, session: requests.Session) -> str:
        prefix = "http://matrixcatalog.co.il/"
        url = prefix + "NBCompetitionRegulations.aspx"
        req_res: requests.Response = requests.get(url)
        soup = BeautifulSoup(req_res.text, features='lxml')
        suffix: str = soup.find('a', href=lambda value: value and category.name.replace('s', '') in value
                                                        and f'-{store_id:03d}-20' in value).attrs['href']
        down_url = prefix + suffix
        print(down_url)
        return down_url

    class XMLFilesCategory(SupermarketChain.XMLFilesCategory):
        All, Promos, PromosFull, Prices, PricesFull, Stores = range(6)

    def __repr__(self):
        return 'CoOp'

    @staticmethod
    def get_items(promo: Tag, items_dict: Dict[str, Item]) -> List[Item]:
        promo_item = items_dict.get(promo.find('ItemCode').text)
        return [promo_item] if promo_item else []
