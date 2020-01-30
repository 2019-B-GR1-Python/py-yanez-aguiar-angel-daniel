# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EmpleosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    empresa = scrapy.Field()
    localizacion = scrapy.Field()
    jornada = scrapy.Field()
    contrato = scrapy.Field()
    salario = scrapy.Field()
