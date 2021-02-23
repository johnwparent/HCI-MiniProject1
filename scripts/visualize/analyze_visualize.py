import os, sys, argparse, csv
import clean_data, visualizer

def main(args):
    parser = argparse.ArgumentParser(description="Parse and Visualize interface data")
    parser.add_argument('-DIR', dest="data_dir", type=str,)
    parse_args = parser.parse_args(args)
    cleaner = clean_data.DictCleaner()
    data = dict()
    cleaner.readAndParse(data, parse_args.data_dir)
    # visualizer.compose_data(parse_args.data_dir)


if __name__ == '__main__':
    main(sys.argv[1:])
