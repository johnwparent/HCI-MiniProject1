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
        self.color_count_correct = {}
        self.color_incorrect_time_agg = {}

    def condition(self, line, linenum):
        return linenum > 2

    # amalgamate a value for each color of the parsed csv -
    # basically, have a tuple count and sum - use class value
    def parse_func(self, sample, selection, linenum):
        color_sample = sample['Color']
        selection_color = selection['Color']
        self.data_points += 1
        if color_sample in self.color_count:
            self.color_count[color_sample] += 1
        else:
            self.color_count[color_sample] = 1
        if color_sample in self.color_count_correct:
            if color_sample == selection_color:
                self.color_count_correct[color_sample] +=1
        else:
            if color_sample == selection_color:
                self.color_count_correct[color_sample] = 1
        time_differential = float(selection['Time']) - float(sample['Time'])
        if color_sample == selection_color:
            if color_sample in self.color_time_agg:
                self.color_time_agg[color_sample] += time_differential
            else:
                self.color_time_agg[color_sample] = time_differential
        else:
            if color_sample in self.color_incorrect_time_agg:
                self.color_incorrect_time_agg[color_sample] += time_differential
            else:
                self.color_incorrect_time_agg[color_sample] = time_differential

    def print_data(self):
        print(self.data_points)
        print(self.color_count)
        print(self.color_time_agg)
        print(self.color_count_correct)

    def iterate_data(self, data):
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
        self.print_data()