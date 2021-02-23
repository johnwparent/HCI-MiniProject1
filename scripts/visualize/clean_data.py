import csv
import os, sys


class Cleaner(object):
    def __init__(self):
        pass

    def condition(self, line):
        pass

    def parse_func(self, line):
        pass

    def clean(self, data, dir_):
        fmtparams = {}
        with open(dir_, 'r', newline='') as exp_data:
            data_reader = csv.reader(exp_data, dialect='excel', **fmtparams)
            self.iterate_data(data_reader)

    def iterate_data(self, data):
        for line in data:
            if self.condition(line):
                self.parse_func(line)

    def readAndParse(self, data:dict):
        pass

class DictCleaner(Cleaner):
    def __init__(self):
        super().__init__()
        self.data_points = 0
        self.color_count = {}
        self.color_time_agg = {}

    def condition(self, line, linenum):
        return linenum > 2

    # amalgamate a value for each color of the parsed csv -
    # basically, have a tuple count and sum - use class value
    def parse_func(self, sample, selection, linenum):
        print(sample)
        print(selection)

    def iterate_data(self, data):
        print(data.fieldnames)
        for line in data:

            if self.condition(line, data.line_num):
                try:
                    select = next(data)
                    self.parse_func(line, select, data.line_num)
                except StopIteration:
                    pass

    def clean(self, data, dir_):
        fmtparams = {}
        with open(dir_, 'r', newline='') as exp_data:
            data_reader = csv.DictReader(exp_data, dialect='excel', **fmtparams)
            self.iterate_data(data_reader)

    def readAndParse(self, data:dict, dir_:str):
        self.clean(data, dir_)