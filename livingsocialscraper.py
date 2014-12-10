from scrapy.item import Item, Field

from scraper_app.items import LivingSocialDeal


class LivingSocialDeal(Item):
	"""Livingsocial container"""

	title = Field()
	description = Field()
	link = Field()
	category = Field()
	location = Field()
	original_price = Field()
	price = Field()

class LivingSocialSpider(BaseSpider):
	"""spider for taking down deal updates"""
	name = 'livingsocial'
	allowed_domains = ['livingsocial.com']
	start_urls = ['http://www.livingsocial.com/cities/15-san-francisco']

	deals_list_xpath = '//li[@dealid]'
	items_fields = {'title': './/adiv[@class="deal-bottom"]/p/text()',
					'link': './/a/@href',
					'description': './/a/div[@class="deal-top"]/div[@class="deal-category"]/span/text()',
					'location' : './/a/div[@class="deal-top"]/ul[@class="unstyled deal-info"]/li/text()',
					'original_price' : './/a/div[@class="deal-bottom"]/ul[@class="unstyled deal-info"]/li[@class="deal-original"]/del/text()',


	}