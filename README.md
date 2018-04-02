#Web crawler, scrapy
This is the scraper to crawl the cochiport expected vessel data

To start this scraper, first make sure you install the scrapy

Open the folder in terminal, then type: scrapy crawl cochiportspider

You will get the list of data in cochiport_data_utf-8.json, the file under cochiport/cochiport/spiders  folder

Data format is json

The pros of this scraper is simple and easy for use, the cons are obivous, this scraper can only be used for this exact data, it is not a good structure to utlize on other website. And there is no error detect and log module in the code.


