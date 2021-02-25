import os, sys, argparse, csv
import clean_data, visualizer

def main(args):
    # doing baseline first then updated in cmd arguements
    parser = argparse.ArgumentParser(description="Parse and Visualize interface data")
    parser.add_argument('-DIR', dest="data_dirs", type=str,nargs='+')
    parse_args = parser.parse_args(args)
    cleanerBaseline = clean_data.DictCleaner()
    data = dict()
    cleanerBaseline.readAndParse(data, parse_args.data_dirs[0])
    cleanerUpdated = clean_data.DictCleaner()
    cleanerUpdated.readAndParse(data, parse_args.data_dirs[1])
    data_baseline = visualizer.compose_data(cleanerBaseline, 'False')
    data_updated = visualizer.compose_data(cleanerUpdated, 'True')
    frames = visualizer.concat(data_baseline, data_updated)

    # seeing reaction time for correct/incorrect selections?? Each interface (i don't think this is necessary)
    #visualizer.generate_barplot(data_baseline, 'correct') 
    #visualizer.generate_barplot(data_updated, 'correct') 
    
    #comparing reaction times across interfaces. Correct/incorrect data??? (working)
    #visualizer.generate_reaction_time_barplot(frames, 'baseline') 

    # printing out reaction times for both interfaces (working)
    #visualizer.gather_mean(cleanerBaseline)
    #visualizer.gather_mean(cleanerUpdated)
    #print()
    # printing out std devs for both interfaces (working)
    #visualizer.gather_stdev(cleanerBaseline)
    #visualizer.gather_stdev(cleanerUpdated)

    # printing overall accuracy and accuracy of each color (Baseline data doesn't make sense)
    avgBaseline, percentBaseline = visualizer.compute_percent_correct(cleanerBaseline)
    avgUpdated, percentUpdated = visualizer.compute_percent_correct(cleanerUpdated)
    
    
    #acc_frame_Baseline = visualizer.compose_accuracy_data(cleanerBaseline, percentBaseline, "False")
    #acc_frame_Updated = visualizer.compose_accuracy_data(cleanerUpdated, percentUpdated, "True")
    #acc_frames = visualizer.concat(acc_frame_Baseline, acc_frame_Updated)
    #visualizer.generate_accuracy_barplot(acc_frames, "baseline")
    #visualizer.generate_box_plot(data_baseline)

if __name__ == '__main__':
    main(sys.argv[1:])
