from typing import Any, Iterable
import scrapy
from scrapy.loader import ItemLoader
import scrapy.resolver
from zabuacrop.items import ZabuacropItem
from scrapy.exceptions import CloseSpider


class ZabuaCrop(scrapy.Spider):
    name = "Company_name"
    handle_httpstatus_list = [404,500,503]
    
    allowed_domains=['www.startupwala.com','www.zaubacorp.com']
    start_urls = ['https://www.startupwala.com/list-of-registered-companies-in-india-P1']
    page_number = 1

    def __init__(self, name: str | None = None, **kwargs: Any):
        super().__init__(name, **kwargs)

    
    def parse(self,response):
        if response.status in (404,500) :
            raise CloseSpider(f'Recieve {response.status} response')
        
        table = response.css("#tableContainer")

        if len(table) == 0:
            raise CloseSpider('No quotes in response')


        for tr in table.css("tr"):
            ZabuaCrop_loader = ItemLoader(item=ZabuacropItem() , selector=tr )

            cin_number = tr.css('td.corporateIdentificationNumber a::text').get()

            if cin_number:
                ZabuaCrop_loader.add_css('company_title','td.companyName a::text')

                ZabuaCrop_loader.add_css('cin_number','td.corporateIdentificationNumber a::text')

                ZabuaCrop_loader.add_css('roc_name','td.roc::text')

                ZabuaCrop_loader.add_css('status','td.statusLink a::text')


                yield ZabuaCrop_loader.load_item()

        self.page_number += 1
        next_page = f'https://www.startupwala.com/list-of-registered-companies-in-india-P{self.page_number}/'
        yield response.follow(next_page, callback=self.parse)
    

            

    