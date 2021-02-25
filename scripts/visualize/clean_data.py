import csv
import os, sys


class Cleaner(object):                  # Reads in data to put into DictCleaner
    def __init__(self):                 # not used
        pass

    def condition(self, line):          # not used
        pass

    def parse_func(self, line):         # not used
        pass

    def clean(self, data, dir_):        # reads data into cleaner from directory and stores in data_reader
        fmtparams = {}                  # not used
        with open(dir_, 'r', newline='') as exp_data:
            data_reader = csv.reader(exp_data, dialect='excel', **fmtparams)
            self.iterate_data(data_reader)

    def iterate_data(self, data):       # iterates through 
        for line in data:
            if self.condition(line):
                self.parse_func(line)

    def readAndParse(self, data:dict):
        pass

class DictCleaner(Cleaner):  
    def __init__(self):   # takes in cleaner object and assigns values to a dictionary
        super().__init__()                      # this is for each color
        self.data_points = 0                    # total number of data points collected (for each experiment) 
        self.color_count = {}                   # Number of times color is shown as sample
        self.color_time_agg = {}                # Aggregate reaction time when color is selected correctly
        self.color_count_correct = {}           # Number of times color is selected correctly
        self.color_incorrect_time_agg = {}      # Aggregate reaction time when color is selected incorrectly

        self.color_count_list = {}              # 
        self.color_count_incorrect_list = {}    # Number of times color is selected incorrectly
    def condition(self, line, linenum):
        return linenum > 2

    # amalgamate a value for each color of the parsed csv -
    # basically, have a tuple count and sum - use class value
    def parse_func(self, sample, selection, linenum):
        color_sample = sample['Color']              # read in sample and selection colors and update data.points
        selection_color = selection['Color']
        self.data_points += 1                       
        if color_sample in self.color_count:        # if color sample count is already in dict, add to it
            self.color_count[color_sample] += 1     
        else:                                       # if not, create it
            self.color_count[color_sample] = 1      
        if color_sample in self.color_count_correct:    # if correct selection count is already in dict, add to it if selection is correct
            if color_sample == selection_color:
                self.color_count_correct[color_sample] +=1
        else:                                           # if not, create it
            if color_sample == selection_color:
                self.color_count_correct[color_sample] = 1

        time_differential = float(selection['Time']) - float(sample['Time'])    # calculates reaction time

        if color_sample == selection_color:                                     # if color selection is correct
            if color_sample in self.color_time_agg:                             # if we have an aggregate time value in the dict, add rxn time to aggregate
                self.color_time_agg[color_sample] += time_differential  
            else:
                self.color_time_agg[color_sample] = time_differential           # if not, create it
        else:                                                                   # if color selection is incorrect, do the same with incorrect data
            if color_sample in self.color_incorrect_time_agg:
                self.color_incorrect_time_agg[color_sample] += time_differential
            else:
                self.color_incorrect_time_agg[color_sample] = time_differential

        if color_sample not in self.color_count_list:                           # creating color count object if it doesn't exist
            self.color_count_list[color_sample] = []
        if color_sample not in self.color_count_incorrect_list:                 # same with incorrect
            self.color_count_incorrect_list[color_sample] = []

        if color_sample == selection_color:
            self.color_count_list[color_sample].append(time_differential)       # adding rxn time to list for the color
        else:
            self.color_count_incorrect_list[color_sample].append(time_differential)

    def print_data(self):   #self explanatory
        print(self.data_points)
        print(self.color_count)
        print(self.color_time_agg)
        print(self.color_count_correct)

    def iterate_data(self, data):   #iterates throught data dictionary, making sure there is a next line before parsing it. Stops when no next line
        for line in data:

            if self.condition(line, data.line_num):
                try:
                    select = next(data)
                    self.parse_func(line, select, data.line_num)
                except StopIteration:
                    pass

    def clean(self, data, dir_):    # reads in data from csv file given directory and assignes it to data?
        fmtparams = {}
        with open(dir_, 'r', newline='') as exp_data:
            data_reader = csv.DictReader(exp_data, dialect='excel', **fmtparams)
            self.iterate_data(data_reader)

    def readAndParse(self, data:dict, dir_:str):    #calls clean function on csv file
        self.clean(data, dir_)
        # self.print_data()