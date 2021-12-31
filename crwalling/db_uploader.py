import os
import django
import csv
import sys

import pandas as pd
from icecream import ic

from common.models import ValueObject, Printer, Reader
from crwalling.models import Today, Week_avg

class Uploader():
    def __init__(self):
        pass
    def new_csv(self, payload:str):
        vo = ValueObject()
        reader = Reader()
        self.printer =Printer()
        vo.context = 'crwalling/data/'
        vo.fname = payload
        self.csvfile = reader.new_file(vo)

        return self.csvfile




    def insert_data(self):
        self.insert_today()
        self.insert_week()

    def insert_today(self):
        with open(self.new_csv('today_case.csv'), newline='', encoding='utf8') as c:
            data_reader = csv.DictReader(c)
            for row in data_reader:
                Today.objects.create(death=row['death'],
                                     serious=row['serious'],
                                     new_hospitalization=row['new_hospitalization'],
                                     confirmed=row['confirmed'],
                                     update_at=row['update_at'])
    def insert_week(self):
        with open(self.new_csv('week_case.csv'), newline='', encoding='utf8') as c:
            data_reader = csv.DictReader(c)
            for row in data_reader:
                Week_avg.objects.create(death=row['death'],
                                     serious=row['serious'],
                                     new_hospitalization=row['new_hospitalization'],
                                     confirmed=row['confirmed'],
                                     update_at=row['update_at'])