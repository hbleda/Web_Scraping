# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Peliculas(scrapy.Item):
    # define the fields for your item here like:
      pelicula = scrapy.Field()
      distribuidora = scrapy.Field()
      taquilla_EEUU = scrapy.Field()
      taquilla_no_EEUU = scrapy.Field()
      recaudacion_mundial = scrapy.Field()
      presupuesto = scrapy.Field()
      anyo_estreno = scrapy.Field()
      director = scrapy.Field()

    
