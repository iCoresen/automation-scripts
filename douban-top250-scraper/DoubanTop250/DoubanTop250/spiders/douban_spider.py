import scrapy
from ..items import Doubantop250Item  # 导入Item类

class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def start_requests(self):
        for i in range(0, 250, 25):
            url = f"https://movie.douban.com/top250?start={i}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movie_items = response.css('div.item')

        for item in movie_items:
            movie_item = Doubantop250Item()

            # 序号
            movie_item['serial_number'] = item.css('em::text').get()

            # 电影名称
            titles = item.css('span.title::text').getall()
            other = item.css('span.other::text').get()
            all_titles = titles + ([other] if other else [])
            movie_item['movie_name'] = ' / '.join([
                t.replace('\xa0', ' ').strip().strip('/') for t in all_titles if t.strip()
            ])

            # 简介
            intro = item.css('div.bd p:first-child::text').getall()
            movie_item['introduction'] = ' '.join([
                i.replace('\xa0', ' ').replace('\n', '').strip() for i in intro if i.strip()
            ])

            # 评分
            movie_item['rating_num'] = item.css('span.rating_num::text').get()

            # 评价人数
            comment_text = item.css('span::text').re(r'(\d+)人评价')
            movie_item['comment_num'] = comment_text[0] if comment_text else None

            # 引言（短评）
            quote = item.css('p.quote span::text').get()
            movie_item['quote'] = quote.strip() if quote else ''

            yield movie_item