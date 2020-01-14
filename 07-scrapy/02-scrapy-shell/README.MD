# scrapy
## scrapy instalacion
ejecutar dentro del `anaconda prompt`.
```
$ conda install -c conda-forge scrapy
```

## comandos generales
```
$ scrapy bench
```
da `las caracterisiticas` para poder hacer Web Scraping o Web Crawling de ese computador
```
$ scrapy settings
```
visualizar las `configuraciones extra`
```
$ scrapy version
```
visualizar la version del scrapy

### scrapy view `url`
`vizualizar el contenido` como lo ve el scrapy
si se ve el contenido
```
$ scrapy view https://www.pluralsight.com/authors
```
no se ve el contenido
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```
### scrapy shell `url`
permite `interactuar con la respuesta` del scrapy mediante un `shell`
```
$ scrapy shell http://quotes.toscrape.com/
```
```
$ response.css('title')
$ response.css('title').extract()
$ response.css('title::text').extract()
$ response.css('.author').extract()
$ response.css('.author::text').extract()
$ type(response.css('.author::text'))
$ response.css('.author::text').extract()[0]
$ response.css('.author::text')[0]
$ type(response.css('.author::text')[0])
$ response.css('.author::text')[0].extract()
$ response.css('.author').extract_first()
$ response.css('span.text::text').extract()
$ response.css('div.tags>a.tag::text').extract()
$ response.css('div.quote>span>a::attr(href)').extract()
$ response.css('.row > div > div:nth-child(2) > .text::text').extract()
$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()

```
## scrapy startproject `nombre_proyecto`
```
$ scrapy startproject arania_basica