from icrawler.builtin import GoogleImageCrawler
import os
import json


class CDiscountImageCrawler(object):

    def __init__(self, class_file):
        self.class_file = class_file
        self.classes = {}
        self.classes_to_dir = {}
        self.parse_class_file()

    def parse_class_file(self):
        for i, line in enumerate(open(self.class_file)):
            if i == 0:
                continue
            tokens = line.split(',')
            self.classes[int(tokens[0])] = tokens[-1][:-1]

    def crawl_keyword(self, classe_index):
        keyword = self.classes[classe_index]
        image_directory = '/home/amor/Documents/databases/image_{}'.format(keyword)
        self.classes_to_dir[classe_index] = image_directory
        if not os.path.exists(image_directory):
            os.mkdir(image_directory)
        google_crawler = GoogleImageCrawler(parser_threads=2,
                                            downloader_threads=4,
                                            storage={'root_dir': image_directory
                                                     })
        google_crawler.crawl(keyword, max_num=100,
                             min_size=(200,200),
                             max_size=None)

    def run(self):
        for img_class in self.classes.keys():
            self.crawl_keyword(img_class)

config_file = "./category_names.csv"
c_crawler = CDiscountImageCrawler(config_file)
c_crawler.run()
json.dumps(c_crawler.classes_to_dir, open("classes_to_dir.json", "w"))
