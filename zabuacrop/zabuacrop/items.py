from scrapy import Item , Field
from itemloaders.processors import TakeFirst , MapCompose

def remove_spaces(txt):
    if txt is not None:
        return txt.strip()

def remove_symbol(txt):
    try:
        if txt is not None:
            return txt.replace("₹","")
    except:
        return txt
    
class ZabuacropItem(Item):
    company_title = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    cin_number = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    roc_name = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    status = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # registration_number = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # company_category = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # company_sub_category = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # class_of_company = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # date_of_incorporation = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # age_of_company = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # activity = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # number_of_members = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # authorised_capital = Field(input_processor=MapCompose(remove_symbol),output_processor=TakeFirst())
    # paid_up_capital = Field(input_processor=MapCompose(remove_symbol),output_processor=TakeFirst())
    # number_of_employees = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # listing_status = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # date_of_last_annual_general_meeting = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # date_of_latest_balance_sheet = Field(input_processor=MapCompose(remove_spaces),output_processor=TakeFirst())
    # email = Field()
    # website = Field()
    # address = Field(output_processor=TakeFirst())
    # created_at = Field(output_processor=TakeFirst())
