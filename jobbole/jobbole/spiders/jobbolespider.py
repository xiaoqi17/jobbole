# -*- coding: utf-8 -*-
import re
import scrapy
from jobbole.items import JobboleItem


class JobbolespiderSpider(scrapy.Spider):
    name = "jobbolespider"
    allowed_domains = ["http://blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        sels = response.css('#archive')
        for sel in sels:
            item = JobboleItem()
            url = sel.css('a.archive-title::attr(href)').extract()[0]
            item['url'] = url
            yield scrapy.Request(url,meta={'item':item}, callback=self.parse2, dont_filter=True)

        next_page = response.css('#archive div.navigation.margin-20 a.next.page-numbers::attr(href)').extract()[0]
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)

    def parse2(self,response):
        item = response.meta['item']
        item['title'] = response.css('div.entry-header h1::text').extract()[0]
        item['create_date'] = response.css('div.entry-meta p::text').re(r'\d+/\d+/\d+')[0]
        item['tag'] = response.css('div.entry-meta p a::text').extract()[0]
        pattern = re.compile('<div class="textwidget"></div>(.*?)<div class="post-adds">', re.S)
        item['content'] = pattern.findall(response.text)[0]
        item['praise_nums'] = response.css('span.btn-bluet-bigger.href-style.bookmark-btn.register-user-only').re(r'\d+')[0]
        item['fav_nums'] = response.css('span.btn-bluet-bigger.href-style.bookmark-btn.register-user-only').re(r'\d+')[3]
        yield item

