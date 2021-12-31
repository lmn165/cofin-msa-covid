import os
import django
import csv
import sys

import pandas as pd
from icecream import ic

from common.models import ValueObject, Printer, Reader
from googledrive.models import drive

class DbUploader():
    def __init__(self):
        pass
    def new_csv(self, payload:str):
        vo = ValueObject()
        reader = Reader()
        self.printer =Printer()
        vo.context = 'googledrive/data/'
        vo.fname = payload
        self.csvfile = reader.new_file(vo)

        return self.csvfile




    def insert_data(self):
        self.insert_case()
    def insert_case(self):
        with open(self.new_csv('pred.csv'), newline='', encoding='utf8') as c:
            data_reader = csv.DictReader(c)
            for row in data_reader:
                drive.objects.create(date=row['0'],
                                    confirmed=row['1'],)