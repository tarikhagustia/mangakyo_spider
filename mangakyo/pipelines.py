# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.utils.python import to_bytes
from urllib.parse import urlparse
class MangakyoPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import hashlib

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if 'image_urls' in item:
        
            for image_url in item['image_urls']:
                request = scrapy.Request(url=image_url)
                request.meta['name'] = item['name']
                yield request

    def file_path(self, request, response=None, info=None):
    
        filename = request.url.split('/')[-1]
        filedir = request.meta['name']
        filepath = filedir + "/" + filename
        return filepath