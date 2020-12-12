import sys

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher

from test import TestSpider
import requests
import re

token = "5fbcebf9-082d-470d-90af-3e4fa7be98d1"
headers = {"Authorization": "Bearer " + token}


def search_for_item(query):
    re.sub('[æÆ]', '%C3%A6', query)
    re.sub('[øØ]', '%C3%B8', query)
    re.sub('[åÅ]', '%C3%A5', query)
    re.sub(' ', '%20', query)
    result = requests.get("https://api.sallinggroup.com/v1-beta/product-suggestions/relevant-products?query=" + query, headers=headers)
    titleToSeachFor = result.json()['suggestions'][0]['title']
    re.sub(" ", "-", titleToSeachFor)
    return [result.json()['suggestions'][0]['prod_id'], titleToSeachFor]


def spider_results(pid, name):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)
    process = CrawlerProcess(get_project_settings())
    TestSpider.prod_id = pid
    TestSpider.title = name
    process.crawl(TestSpider)
    process.start()
    return results


def find_ingredients(product):
    q = search_for_item()
    ingredients = spider_results(q[0], q[1])[0]['ingredients']
    print(q[1] + " - " + ingredients)


if __name__ == '__main__':
    print("hello")