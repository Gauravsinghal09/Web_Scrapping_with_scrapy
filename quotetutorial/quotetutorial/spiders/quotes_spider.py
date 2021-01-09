import scrapy
from scrapy import FormRequest

from ..items import QuotetutorialItem


class QuoteSpidet(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        # print('Token: ' + token)
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'vsvvsvv',
            'password': 'vsvswgv'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        all_titles = response.css(".quote")
        items = QuotetutorialItem()
        for quotes in all_titles:
            items['title'] = quotes.css(".text::text").extract()
            items['author'] = quotes.css(".author::text").extract()
            items['tag'] = quotes.css(".tag::text").extract()
            yield items

        next_url = response.css('.next a::attr(href)').get()

        print('Next Page: ' + next_url)

        if next_url is not None:
            yield response.follow(next_url, callback=self.parse)
