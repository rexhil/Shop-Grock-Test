import scrapy


class GetGrocery(scrapy.Spider):
    name = "grocery"

    def start_requests(self):
        url = "https://www.aldi.com.au/"
        yield scrapy.Request(url=url, callback=self.parse_grocery)

    def parse_grocery(self, response):
        main_menus = response.selector.xpath('//ul[@role="menubar"]/li')
        for main_menu in main_menus:
            if main_menu.xpath("div[1]/a[2]/text()").get() == "Groceries":
                menu_urls = main_menu.xpath('div[2]/ul/li/div/a[@role="menuitem"]/@href').getall()
                for url in menu_urls:
                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.selector.xpath('//div[@class="box m-text-image"]/div')
        for product in products:
            product_price_selector = product.xpath('div[2]/div[@class="box--price"]')
            yield {
                'product_title': product.xpath('div[2]/div[@class="box--description--header"]/text()').get().strip(),
                'product_image': product.xpath('div[1]/img/@src').get(),
                'pack_size': product_price_selector.xpath('span[@class="box--amount"]/text()').get(),
                'value_price': product_price_selector.xpath('span[@class="box--value"]/text()').getall(),
                'decimal_price': product_price_selector.xpath('span[@class="box--decimal"]/text()').get(),
                'price_per_unit': product_price_selector.xpath('span[@class="box--baseprice"]/text()').get()
            }










