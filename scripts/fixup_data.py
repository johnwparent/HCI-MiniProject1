import sys, csv, argparse, collections

def read_in_data(dir):
    good_data = {}
    with open(dir, mode='r') as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            good_data[row['Time']] = row
    return good_data

def sort_data(data):
    good_data_ = sorted(data.items(),key=lambda t: float(t[0]))
    return  good_data_

def write_back(dir_,data):
    with open(dir_, mode='w',newline='') as out_file:
        writer = csv.DictWriter(out_file,fieldnames=["Color","Time","Type"],dialect='excel')
        writer.writeheader()
        for row in data:
            writer.writerow(row[1])

def main(args):
    cmd_args = argparse.ArgumentParser()
    cmd_args.add_argument("--file",dest='dir',action='store')
    command_args = cmd_args.parse_args(args)
    data = read_in_data(command_args.dir)
    s_data = sort_data(data)
    write_back(command_args.dir, s_data)

if __name__ == '__main__':
    main(sys.argv[1:])