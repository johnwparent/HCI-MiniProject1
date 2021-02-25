import seaborn as sns, pandas as pd, statistics
import matplotlib.pyplot as plt
from clean_data import DictCleaner

def compute_percent_correct(read_data: DictCleaner):
    correctness = {}                                                   # creating correctness dict to store value for each color
    for color in read_data.color_count:
        if color in read_data.color_count_correct and read_data.color_count[color]:                             #if color(ex: red) has a color count/correct count in dict
            correctness[color] = int(read_data.color_count_correct[color])/int(read_data.color_count[color])    #correctness = # correct selections/# times shown
        else:
            correctness[color] = 0
    avg_correct = sum(correctness.values())/len(correctness)            # calculates sum of (accuracy/ #number of colors) for each color??? This is the average
    print()
    print("The average accuracy for all of the colors is " )
    print(avg_correct)
    print()
    for color in correctness:
        print("The accuracy of the user's selection of %s  is: " % color)
        print(correctness[color])
    print()
    return avg_correct, correctness                 # returns correctness for each color and aggregate correctness

def concat(*args):           # duh
    cat_list = []
    for arg in args:
        cat_list.append(arg)

    return pd.concat(cat_list)

def compute_stddev(timing_dict):    # creates standard dev dict and stores std devs for each color
    stddev_dict = dict()
    for key in timing_dict:
        if timing_dict[key]:
            stddev_dict[key] = statistics.pstdev(timing_dict[key])
    return stddev_dict

def gather_stdev(read_data: DictCleaner):       # uses compute_stddev to get correct and incorrect std devs
    correct_stddev = compute_stddev(read_data.color_count_list)
    incorrect_stddev = compute_stddev(read_data.color_count_incorrect_list)
    print()
    print("The standard dev for correct selections was:")
    print(correct_stddev)
    print("The standard dev for incorrect selections was:")
    print(incorrect_stddev)
    print()

def compute_mean(total, agg):                       # compute mean using total and aggregate of something
    mean_dict = dict()
    for color in agg:
        mean_dict[color] = float(agg[color])/float(total[color])        # mean = aggregate /number of occurances
    return mean_dict

def gather_mean(read_data: DictCleaner):
    correct_mean_dict = compute_mean(read_data.color_count_correct,read_data.color_time_agg)    # computes average reaction time for correct selections for each color in a dataset
    incorrect_count = {}
    for color in read_data.color_count:                                                         # computes incorrect count for each color
        if color in read_data.color_count_correct and read_data.color_count[color]:
            incorrect_count[color] = float(read_data.color_count[color]) - float(read_data.color_count_correct[color])
        else:
            incorrect_count[color] = float(read_data.color_count[color])
    incorrect_mean_dict = compute_mean(incorrect_count,read_data.color_incorrect_time_agg)      # computes average reaction time for incorrect selections
    print()
    print("The average reaction time for correct selections was: ")
    print(correct_mean_dict)
    print("The average reaction time for incorrect selections was ")
    print(incorrect_mean_dict)
    print()

def compose_data(read_data, baseline):                                      # creates dataframe to store reaction time data and organizes it
    columns = ['color','time','correct', 'baseline']
    data = []
    for color in read_data.color_count:                                      # for each color
        for time_val in read_data.color_count_list[color]:  
            data.append([color,time_val,"True",baseline])                   # adds a row to the dataframe: color, reaction time, correct bool, baseline bool
    for color in read_data.color_count_incorrect_list:
        for incorrect_count_val in read_data.color_count_incorrect_list[color]:
            data.append([color,incorrect_count_val,"False",baseline])

    frame_data = pd.DataFrame(data=data,columns=columns)                    # putting data from reader into a dataframe for seaborn to use
    # print(frame_data)
    return frame_data

def compose_accuracy_data(read_data, agg_data, baseline):               # putting accuracy data in a dataframe 
    columns = ['color','accuracy','baseline']
    data = []
    for color in read_data.color_count:                                 # adds a row to the dataframe: color,  aggregate accuracy data, baseline bool
        data.append([color, agg_data[color], baseline])

    frame_data = pd.DataFrame(data=data, columns=columns)
    return frame_data

def generate_accuracy_barplot(data, grouping):                                                        # edit formatting!!!!!
    sns.barplot(x='color',y='accuracy',hue=grouping,data=data)
    plt.xlabel("Colors")
    plt.ylabel("Accuracy")
    plt.title("Accuracy: Natasha ")
    #plt.legend(title="Interface") #, labels=[""])
    plt.show()

def generate_reaction_time_barplot(data, grouping):                                                        # edit formatting!!!!!
    sns.barplot(x='color',y='time',hue=grouping,data=data)
    plt.xlabel("Colors")
    plt.ylabel("Avg Reaction Time")
    #plt.title("Avg Reaction Time Across Interfaces: Natasha")
    #plt.legend(title="Interface", labels=["Baseline", "Updated"]) #check label order
    plt.show()

def generate_box_plot(data):                                                        # edit formatting!!!!!
    sns.boxplot(x='color',y='time',hue='correct',hue_order=['True'],data=data)
    plt.xlabel("Colors")
    plt.ylabel("Avg Reaction Time")
    plt.title("Avg Reaction Time: Natasha ")
    #plt.legend(title="Interface", labels=["Baseline","Updated"])
    plt.show()