import scrapy

def guardar_archivo(titulo, link, precio):
    import csv
    with open('libros.csv','a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(titulo, link, precio))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)
    print("listo :)")

class introSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [#'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
    #'http://books.toscrape.com/index.html',
    'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
    'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
    'http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
    'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
    'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html',
    'http://books.toscrape.com/catalogue/category/books/classics_6/index.html',
    'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
    'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
    'http://books.toscrape.com/catalogue/category/books/romance_8/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
    'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
    'http://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html',
    'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
    'http://books.toscrape.com/catalogue/category/books/childrens_11/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html',
    'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-4.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-5.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-6.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-7.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/page-8.html',
    'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
    'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
    'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
    'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-4.html',
    'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
    'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
    'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
    'http://books.toscrape.com/catalogue/category/books/young-adult_21/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/young-adult_21/page-3.html',
    'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
    'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
    'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
    'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
    'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
    'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
    'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
    'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
    'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
    'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
    'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
    'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
    'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html',
    'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
    'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
    'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
    'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
    'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
    'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
    'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
    'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
    'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
    'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
    'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
    'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
    'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
    'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
    'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
    'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
    'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
    'http://books.toscrape.com/catalogue/category/books/crime_51/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        """
        enlaces = response.css('div.side_categories>ul>li>ul>li>a::attr(href)').extract()
        print(enlaces)
        #lista_enlaces=[]
        for p in enlaces:
            p = 'http://books.toscrape.com/' + p
            print(p)
            #lista_enlaces.append(p)
        #print(lista_enlaces)
        """
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        print(titulos)
        links = etiqueta_contenedora.css('div > a::attr(href)').extract()
        lista_links=[]
        for p in links:
            p = 'http://books.toscrape.com/catalogue' + p[8:]
            lista_links.append(p)
        print(lista_links)
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        lista_precios=[]
        for p in precios:
            p = p[1:]
            lista_precios.append(p)
        [float(i) for i in lista_precios]
        print(lista_precios)

        guardar_archivo(titulos,lista_links,lista_precios)

