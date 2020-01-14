import scrapy
class introSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        print(titulos)
        links = etiqueta_contenedora.css('div > a::attr(href)').extract()
        nuevolink=[]
        for p in links:
            p = 'http://books.toscrape.com/catalogue' + p[8:]
            nuevolink.append(p)
        print(nuevolink)
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()[1:]
        nueva=[]
        for p in precios:
            p = p[1:]
            nueva.append(p)
        [float(i) for i in nueva]
        print(nueva)