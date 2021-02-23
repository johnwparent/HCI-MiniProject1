import seaborn, pandas

def compose_data(read_data):
    frame_csv = pandas.read_csv(read_data)
    for line in frame_csv:
        pass