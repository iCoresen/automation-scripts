# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import xlwt

class CsvPipeline:
    def __init__(self):
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('top250')
        self.sheet.write(0, 0, 'serial_number')
        self.sheet.write(0, 1, 'movie_name')
        self.sheet.write(0, 2, 'introduction')
        self.sheet.write(0, 3, 'rating_num')
        self.sheet.write(0, 4, 'comment_num')
        self.sheet.write(0, 5, 'quote')
        self.row = 1

    def process_item(self, item, spider):
        self.sheet.write(self.row, 0, item['serial_number'])
        self.sheet.write(self.row, 1, item['movie_name'])
        self.sheet.write(self.row, 2, item['introduction'])
        self.sheet.write(self.row, 3, item['rating_num'])
        self.sheet.write(self.row, 4, item['comment_num'])
        self.sheet.write(self.row, 5, item['quote'])

        self.row += 1
        self.close_file(item)

    def close_file(self, item):
        self.book.save('top250.xls')
        return item
