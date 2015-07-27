#-*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from ojcc.items import AccountItem

class SdutAccountSpider(Spider):
    name = 'sdut_user'
    allowed_domains = ['acm.sdut.edu.cn']

    accepted_url = \
        'http://acm.sdut.edu.cn/sdutoj/status.php?\
        username=%s&pro_lang=ALL&result=1'

    solved = {}

    def __init__(self,
            username='15940', *args, **kwargs):
        super(SdutAccountSpider, self).__init__(*args, **kwargs)

        self.username = username
        self.start_urls = [
            'http://acm.sdut.edu.cn/sdutoj/setting.php?userid=%s' % username
        ]

    def parse(self, response):

        sel = Selector(response)

        self.item = AccountItem()
        self.item['origin_oj'] = 'sdut'
        self.item['username'] = self.username

        self.username = sel.\
            xpath('//div[@id="content"]/table/tr')[0].\
            xpath('./td[2]/h2/text()').extract()[0]

        self.item['nickname'] = sel.\
            xpath('//div[@id="content"]/table/tr')[1].\
            xpath('./td[2]/xmp/text()').extract()[0]
        self.nickname = self.item['nickname']

        self.item['rank'] = sel.\
            xpath('//div[@id="content"]/table/tr')[1].\
            xpath('./td[6]/text()').extract()[0]
        self.item['accept'] = sel.\
            xpath('//div[@id="content"]/table/tr')[2].\
            xpath('./td[4]/text()').extract()[0]
        self.item['submit'] = sel.\
            xpath('//div[@id="content"]/table/tr')[3].\
            xpath('./td[6]/text()').extract()[0]
        yield Request(self.accepted_url % self.username,
            callback = self.accepted
        )

        yield self.item

    def accepted(self, response):

        sel = Selector(response)

        next_url = sel.xpath('.//div[@class="page"]/a/@href')[1].extract()
        table_tr = sel.xpath('//table[@class="tablelist"]/tr')[1:]
        for tr in table_tr:
            name = tr.xpath('.//td/a/xmp/text()').extract()[0]
            problem_id = tr.xpath('.//td[3]/a/text()').extract()[0].strip()
            submit_time = tr.xpath('.//td/text()').extract()[-1]

            if name == self.nickname:
                self.solved[problem_id] = submit_time
                self.item['solved'] = self.solved

        if table_tr:
            yield Request(
                'http://' +
                self.allowed_domains[0] +
                '/sdutoj/' +
                next_url,
                callback = self.accepted
            )

        yield self.item
