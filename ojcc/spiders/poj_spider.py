#-*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from ojcc.items import AccountItem

class PojAccountSpider(Spider):
    name = 'poj_user'
    allowed_domains = ['poj.org']

    accepted_url = \
        'http://poj.org/status?problem_id=\
        &user_id=%s&result=0&language='

    download_delay = 1
    solved = {}

    def __init__(self,
            username='sdutacm1', *args, **kwargs):
        super(PojAccountSpider, self).__init__(*args, **kwargs)

        self.username = username

        self.start_urls = [
            "http://poj.org/userstatus?user_id=%s" % username
        ]

    def parse(self, response):
        sel = Selector(response)

        self.item = AccountItem()
        self.item['origin_oj'] = 'poj'
        self.item['username'] = self.username
        self.item['rank'] = sel.xpath('//center/table/tr')[1].\
            xpath('.//td/font/text()').extract()[0]
        self.item['accept'] = sel.xpath('//center/table/tr')[2].\
            xpath('.//td/a/text()').extract()[0]
        self.item['submit'] = sel.xpath('//center/table/tr')[3].\
            xpath('.//td/a/text()').extract()[0]
        yield Request(self.accepted_url % self.username,
            callback = self.accepted
        )

        yield self.item

    def accepted(self, response):

        sel = Selector(response)

        next_url = sel.xpath('//p/a/@href')[2].extract()
        table_tr = sel.xpath('//table')[-1].xpath('.//tr')[1:]
        for tr in table_tr:
            name = tr.xpath('.//td/a/text()').extract()[0]
            problem_id = tr.xpath('.//td[3]/a/text()').extract()[0].strip()
            submit_time = tr.xpath('.//td/text()').extract()[-1]

            self.solved[problem_id] = submit_time
            self.item['solved'] = self.solved

        if table_tr:
            yield Request(
                'http://' +
                self.allowed_domains[0] +
                '/' + next_url,
                callback = self.accepted
            )

        yield self.item
