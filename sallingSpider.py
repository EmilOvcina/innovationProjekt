import scrapy
import re
import json

class SallingspiderSpider(scrapy.Spider):
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'LOG_ENABLED': 'False'
    }

    prod_id = ""
    title = ""

    re.sub('[æÆ]', '%C3%A6', prod_id)
    re.sub('[øØ]', '%C3%B8', prod_id)
    re.sub('[åÅ]', '%C3%A5', prod_id)
    re.sub(' ', '%20', prod_id)

    name = 'sallingSpider'
    start_urls = ['https://www.bilkatogo.dk/produkt/' + title + '/' + prod_id + '/']

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "da - DK, da; q = 0.9, en - US; q = 0.8, en;q = 0.7",
        "Referer": "https://www.bilkatogo.dk/",
        "Origin": "https://www.bilkatogo.dk",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0(Macintosh;Intel Mac OS X 11_0_0) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0.4280.88 Safari / 537.36"
    }

    def parse(self, response):
        url = "https://api.bilkatogo.dk/api/shop/v3/Product?u=w&productId=" + self.prod_id
        req = scrapy.Request(url, callback=self.parse_api, headers=self.headers)
        yield req

    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        yield {
            'ingredients': data['info'][1]['items'][0]['value']
        }
