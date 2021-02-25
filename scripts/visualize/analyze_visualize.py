import os, sys, argparse, csv
import clean_data, visualizer

def main(args):
    parser = argparse.ArgumentParser(description="Parse and Visualize interface data")
    parser.add_argument('-DIR', dest="data_dirs", type=str,nargs='+')
    parse_args = parser.parse_args(args)
    cleanerA = clean_data.DictCleaner()
    data = dict()
    cleanerA.readAndParse(data, parse_args.data_dirs[0])
    cleanerB = clean_data.DictCleaner()
    cleanerB.readAndParse(data, parse_args.data_dirs[1])
    data_a = visualizer.compose_data(cleanerA, 'False')
    data_b = visualizer.compose_data(cleanerB, 'True')
    frames = visualizer.concat(data_a, data_b)
    visualizer.generate_barplot(data_a, 'correct')
    visualizer.generate_barplot(data_b, 'correct')
    visualizer.generate_barplot(frames, 'baseline')
    visualizer.gather_mean(cleanerA)
    visualizer.gather_mean(cleanerB)
    print()
    visualizer.gather_stdev(cleanerA)
    visualizer.gather_stdev(cleanerB)
    aggA, percentA = visualizer.compute_percent_correct(cleanerA)
    aggB, percentB = visualizer.compute_percent_correct(cleanerB)

    acc_frame_a = visualizer.compose_accuracy_data(cleanerA, percentA, "False")
    acc_frame_b = visualizer.compose_accuracy_data(cleanerB, percentB, "True")
    acc_frames = visualizer.concat(acc_frame_a, acc_frame_b)
    visualizer.generate_accuracy_barplot(acc_frames, "baseline")
    visualizer.generate_box_plot(data_a)

if __name__ == '__main__':
    main(sys.argv[1:])
