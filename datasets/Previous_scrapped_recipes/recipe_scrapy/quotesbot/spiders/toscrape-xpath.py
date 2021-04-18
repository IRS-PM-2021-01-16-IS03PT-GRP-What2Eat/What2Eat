# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://mysingaporefood.com/recipes/',
    ]

    def parse(self, response):
        for recipe in response.xpath('//div[@class="brands-listing"]/@href'):
            yield {
                'title': recipe.xpath('//div[@class="chef-recipe-top-text bp-rel fr"]/text()').getall(),
                'ingredient': recipe.xpath('//div[@class="ch-st-ingredients"]/text()').getall(),
                'Methods': recipe.xpath('//div[@class="ch-st-methods"]/text()').getall()
            }

        next_page_url = response.xpath('//ul[@class="page-numbers"]/a/@href').get()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url),callback=self.parse)

