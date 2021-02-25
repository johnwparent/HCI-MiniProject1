import seaborn as sns, pandas as pd, statistics
import matplotlib.pyplot as plt
from clean_data import DictCleaner

def compute_percent_correct(read_data: DictCleaner):
    correctness = {}
    for color in read_data.color_count:
        if color in read_data.color_count_correct and read_data.color_count[color]:
            correctness[color] = int(read_data.color_count_correct[color])/int(read_data.color_count[color])
        else:
            correctness[color] = 0
    agg_correct = sum(correctness.values())/len(correctness)
    print()
    print(agg_correct)
    print()
    for color in correctness:
        print(color)
        print(correctness[color])
    print()
    return agg_correct, correctness

def concat(*args):
    cat_list = []
    for arg in args:
        cat_list.append(arg)

    return pd.concat(cat_list)

def compute_stddev(timing_dict):
    stddev_dict = dict()
    for key in timing_dict:
        if timing_dict[key]:
            stddev_dict[key] = statistics.pstdev(timing_dict[key])
    return stddev_dict

def gather_stdev(read_data: DictCleaner):
    correct_stddev = compute_stddev(read_data.color_count_list)
    incorrect_stddev = compute_stddev(read_data.color_count_incorrect_list)
    print()
    print("stddev")
    print(correct_stddev)
    print(incorrect_stddev)
    print("end stddev")
    print()

def compute_mean(total, agg):
    mean_dict = dict()
    for color in agg:
        mean_dict[color] = float(agg[color])/float(total[color])
    return mean_dict

def gather_mean(read_data: DictCleaner):
    correct_mean_dict = compute_mean(read_data.color_count_correct,read_data.color_time_agg)
    incorrect_count = {}
    for color in read_data.color_count:
        if color in read_data.color_count_correct and read_data.color_count[color]:
            incorrect_count[color] = float(read_data.color_count[color]) - float(read_data.color_count_correct[color])
        else:
            incorrect_count[color] = float(read_data.color_count[color])
    incorrect_mean_dict = compute_mean(incorrect_count,read_data.color_incorrect_time_agg)
    print()
    print("mean")
    print(correct_mean_dict)
    print(incorrect_mean_dict)
    print("end mean")
    print()

def compose_data(read_data, baseline):
    columns = ['color','time','correct', 'baseline']
    data = []
    for color in read_data.color_count:
        for time_val in read_data.color_count_list[color]:
            data.append([color,time_val,"True",baseline])
    for color in read_data.color_count_incorrect_list:
        for incorrect_count_val in read_data.color_count_incorrect_list[color]:
            data.append([color,incorrect_count_val,"False",baseline])

    frame_data = pd.DataFrame(data=data,columns=columns)
    # print(frame_data)
    return frame_data

def compose_accuracy_data(read_data, agg_data, baseline):
    columns = ['color','accuracy','baseline']
    data = []
    for color in read_data.color_count:
        data.append([color, agg_data[color], baseline])

    frame_data = pd.DataFrame(data=data, columns=columns)
    return frame_data

def generate_accuracy_barplot(data, grouping):
    sns.barplot(x='color',y='accuracy',hue=grouping,data=data)
    plt.show()

def generate_barplot(data, grouping):
    sns.barplot(x='color',y='time',hue=grouping,data=data)
    plt.show()

def generate_box_plot(data):
    sns.boxplot(x='color',y='time',hue='correct',hue_order=['True'],data=data)
    plt.show()