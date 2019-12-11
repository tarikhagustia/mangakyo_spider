# -*- coding: utf-8 -*-
import scrapy

from mangakyo.items import MangakyoItem

class MangakyowebSpider(scrapy.Spider):
    name = 'mangakyoweb'
    allowed_domains = ['mangakyo.com']

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', []) 
        if urls:
            self.start_urls = urls.split(',')
        self.logger.info(self.start_urls)
        super(MangakyowebSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
    
        for row in response.xpath("//span[contains(@class, 'lchx')]/a/@href"):
            yield scrapy.Request(row.extract(), callback=self.parse_image) 
    
    def parse_image(self, response):
        comics = []
        item = MangakyoItem()
        for image in response.xpath("//img[contains(@class, 'alignnone')]/@src"):    
            comics.append(image.extract())
        item['name'] = response.xpath("//h1/text()").extract_first()
        item['image_urls'] = comics
    
        yield item