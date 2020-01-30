import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from empleos.items import EmpleosItem
from scrapy.exceptions import CloseSpider

class EmpleosSpider(CrawlSpider):
	name = 'empleos'
	item_count = 0
	allowed_domain = ['www.computrabajo.com.ec']
	start_urls = ['https://www.computrabajo.com.ec/ofertas-de-trabajo/?fbclid=IwAR00DWXoIrgUMKiSYsS6dX-XQUH0ITPSud2Zpfh3ta1b02Iut68EXRURKPI']

	rules = {
		#Rule(LinkExtractor(allow =(), restrict_css =('div.pagination_container > ul > li.andes-pagination_button--next > a'))),
		Rule(LinkExtractor(allow =(), restrict_css =('div.pg_grid > a.next'))),
		Rule(LinkExtractor(allow =(), restrict_css =('div.gO > div > div.iO > h2.tO > a')),
			callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		b_item = EmpleosItem()
		b_item['titulo'] = response.xpath('//section[@class="box box_r"]/ul/li[1]/p//text()').extract()
		b_item['empresa'] = response.xpath('//section[@class="box box_r"]/ul/li[2]/p//text()').extract()
		b_item['localizacion'] = response.xpath('//section[@class="box box_r"]/ul/li[3]/p//text()').extract()
		b_item['jornada'] = response.xpath('//section[@class="box box_r"]/ul/li[4]/p//text()').extract()
		b_item['contrato'] = response.xpath('//section[@class="box box_r"]/ul/li[5]/p//text()').extract()
		b_item['salario'] = response.xpath('//section[@class="box box_r"]/ul/li[6]/p//text()').extract()
		self.item_count += 1
		if self.item_count > 100000:
			raise CloseSpider('item_exceeded')
		yield b_item