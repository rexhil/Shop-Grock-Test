# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AldiCrawlPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if len(adapter['value_price']) == 2 and adapter['value_price'][1] == 'c':
            try:
                adapter['price'] = float('0.{}'.format(adapter['price'][0]))
            except ValueError as e:
                adapter['price'] = 'err'
        else:
            try:
                price = '{}{}'.format(adapter['value_price'][0], adapter['decimal_price']).strip('$')
                adapter['price'] = float(price)
            except ValueError as e:
                adapter['price'] = 'err'
        del(adapter['value_price'])
        del(adapter['decimal_price'])
        return item
