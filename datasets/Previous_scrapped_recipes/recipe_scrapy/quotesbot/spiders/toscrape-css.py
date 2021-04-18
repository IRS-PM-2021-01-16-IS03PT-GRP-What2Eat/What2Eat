# -*- coding: utf-8 -*-
import scrapy
from pydispatch import dispatcher
import json
from scrapy.http import Request

from scrapy import signals



class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ['https://singaporelocalfavourites.com/category/recipes']
    counter = 0
    results = {}
    
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse(self, response):
        
        
        for quote in response.css('div.post-card__title a::attr(href)'):
            yield scrapy.Request(url=quote.get(), callback=self.parseInnerPage)
            
            nextPage = response.css('nav > div.nav-links > a.next.page-numbers::attr(href)').get()
            if nextPage is not None:
                #response.follow(nextPage,callback=self.parse)
                next_page = response.urljoin(nextPage)
                yield Request(next_page,callback=self.parse)
            
    def parseInnerPage(self,response):
        title = response.css("h1::text").get()
        image = response.css("div.entry-content>p>span>img::attr(data-srcset)").get()
        ingredients = response.css('ul>li::text').getall()
        method = response.css('ol>li::text').getall()
        self.results[self.counter] ={
            "Title": title,
            "Image":image,
            "Ingredients":ingredients,
            "Method":method
            }
        self.counter = self.counter + 1
                
    def spider_closed(self, spider):
        with open('results.json','w') as fp:
            json.dump(self.results,fp)
            