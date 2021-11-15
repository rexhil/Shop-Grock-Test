import scrapy
from urllib.parse import urlparse


class GetGrocery(scrapy.Spider):
    name = "grocery"

    def start_requests(self):
        url = "https://www.aldi.com.au/groceries"
        yield scrapy.Request(url=url, callback=self.parse_grocery)

    def parse_grocery(self, response):
        menu_urls = response.selector.xpath('//div[@class="productworld--container"]/div/div/a/@href').getall()
        for url in menu_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.selector.xpath('//div[@class="box m-text-image"]/div')
        category = response.selector.xpath('//title/text()').get()
        for product in products:
            product_price_selector = product.xpath('div[2]/div[@class="box--price"]')
            yield {
                'product_title': product.xpath('div[2]/div[@class="box--description--header"]/text()').getall(),
                'product_image': product.xpath('div[1]/img/@src').get(),
                'pack_size': product_price_selector.xpath('span[@class="box--amount"]/text()').get(),
                'value_price': product_price_selector.xpath('span[@class="box--value"]/text()').getall(),
                'decimal_price': product_price_selector.xpath('span[@class="box--decimal"]/text()').get(),
                'price_per_unit': product_price_selector.xpath('span[@class="box--baseprice"]/text()').get(),
                'category': category
            }
        if not products:
            url_last = urlparse(response.url).path
            urls = response.selector.xpath('//article[@id="main-content"]/div//a/@href').getall()
            for url in urls:
                if url_last in url:
                    yield scrapy.Request(url=url, callback=self.parse)











