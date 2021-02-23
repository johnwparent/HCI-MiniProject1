import tkinter as tk
import random as random
import csv
import time

def rgb_color_to_hex(rgb_val:tuple):
    r = hex(rgb_val[0])
    g = hex(rgb_val[1])
    b = hex(rgb_val[2])
    return '#{:0<2}{:0<2}{:0<2}'.format(r[r.rfind('x')+1:],g[g.rfind('x')+1:],b[b.rfind('x')+1:])

#creating file to write to
with open('testBaselineData.csv', mode='w', newline='') as csv_file:
    #declaring headers and creating writer object
    myFields=['Color','Time','Type'] #Type is sample or selection
    data_writer = csv.DictWriter(csv_file, delimiter=',',fieldnames=myFields)
    data_writer.writeheader()

#function to log button selections
    #inputs: color selected, time of selection, file to log to
    #outputs: just adds inputs to .csv file
def logSelection(colorToLog, colorType):
    #writing color and time of selection
    #reopening file (to append this time) and redeclaring data_writer(better way to do this?)
    with open('testBaselineData.csv', mode='a', newline='') as csv_file:
        data_writer = csv.DictWriter(csv_file, delimiter=',',fieldnames=myFields)
        timeOfLog = time.monotonic()
        data_writer.writerow({'Color':colorToLog,'Time':timeOfLog,'Type':colorType})
        # changing the sample color if a selection color was clicked
        if colorType == 'selection':
            #generate a random # between 0 and 5 to pull a color from color_ array
            sampleColorInt = random.randint(0,5)
            #wait half a second then change sample color
            time.sleep(0.5)
            sampleColor.config( bg = rgb_color_to_hex(colors_[sampleColorInt]), text = '',
                                  command = logSelection((color_list[sampleColorInt]),'sample'))
      
            

window = tk.Tk()
window.after(180000,window.destroy)

#text declaration at top of window
titleFrame = tk.Frame(master=window,width=200, bg="white")
title = tk.Label(master=titleFrame, font='bold', text= "Potsdam Transportation Company Bus Schedule Manager")
title.pack()
titleFrame.grid(row=0, column=0, columnspan=6)
topLabelFrame = tk.Frame(master=window,width=200,height=100)
topLabel = tk.Label(master=topLabelFrame, text = "Operators: Press route icon associated with the bus that has arrived at the stop to record route delays. Arrivals will be broadcast over headsets or shown at the bottom right.")
topLabel.pack()
topLabelFrame.grid(row=1, column=0, columnspan=6)

#making color frames
colors_ = [
    (255,0,0),
    (56,87,35),
    (127,96,0),
    (255,255,0),
    (0,47,142),
    (112,48,160),
]

color_list = [
    "red",
    "green",
    "brown",
    "yellow",
    "blue",
    "purple",
]

#red button
frm_Red = tk.Frame(master=window,padx=10,pady=10)
Red = tk.Button(master=frm_Red, bg = rgb_color_to_hex(colors_[0]), width=20, height=10,
                command = lambda: logSelection('red','selection')) 
Red.pack()
frm_Red.grid(column=0, row=2)
#green button
frm_Green = tk.Frame(master=window,padx=10,pady=10)
Green = tk.Button(master=frm_Green, bg = rgb_color_to_hex(colors_[1]), width=20, height=10,
                  command = lambda:logSelection('green','selection')) 
Green.pack()
frm_Green.grid(column=1, row=2)
#brown button
frm_Brown = tk.Frame(master=window,padx=10,pady=10)
Brown = tk.Button(master=frm_Brown, bg=rgb_color_to_hex(colors_[2]), width=20, height=10,
                  command = lambda:logSelection('brown','selection'))
Brown.pack()
frm_Brown.grid(column=2, row=2)
#yellow button
frm_Yellow = tk.Frame(master=window,padx=10,pady=10)
Yellow = tk.Button(master=frm_Yellow, bg = rgb_color_to_hex(colors_[3]), width=20, height=10,
                   command = lambda:logSelection('yellow','selection')) 
Yellow.pack()
frm_Yellow.grid(column=3, row=2)
#blue button
frm_Blue = tk.Frame(master=window,padx=10,pady=10)
Blue = tk.Button(master=frm_Blue, bg = rgb_color_to_hex(colors_[4]), width=20, height=10,
                 command = lambda:logSelection('blue','selection')) 
Blue.pack()
frm_Blue.grid(column=4, row=2)
#purple button
frm_Purple = tk.Frame(master=window,padx=10,pady=10)
Purple = tk.Button(master=frm_Purple, bg = rgb_color_to_hex(colors_[5]), width=20, height=10,
                   command = lambda:logSelection('purple','selection')) 
Purple.pack()
frm_Purple.grid(column=5, row=2)


#setting the grid locations for arrival time + delay data
#expected arrival
eaLabelFrame = tk.Frame(master=window,padx=10,pady=10)
eaLabel = tk.Label(master=eaLabelFrame, text = "Expect Arrival: ")
eaLabel.pack()
eaLabelFrame.grid(row=5,column=0)
#actual arrival
aaLabelFrame = tk.Frame(master=window,padx=10,pady=10)
aaLabel = tk.Label(master=eaLabelFrame, text = "Actual Arrival: ")
aaLabel.pack()
aaLabelFrame.grid(row=6,column=0)
#delay
dLabelFrame = tk.Frame(master=window,padx=10,pady=10)
dLabel = tk.Label(master=eaLabelFrame, text = "Delay: ")
dLabel.pack()
dLabelFrame.grid(row=7,column=0)


#setting grid location for sample color
#current bus text box
cbLabelFrame = tk.Frame(master=window,padx=10,pady=10)
cbLabel = tk.Label(master=cbLabelFrame, text = "Current bus at stop")
cbLabel.pack()
cbLabelFrame.grid(row=4, column=4, columnspan=2, sticky = 's')

#creating frame fror sample color (sample color placeholder is replaced by sample color)
frm_Sample = tk.Frame(master=window,padx=10,pady=10)
sampleColor = tk.Label(master=frm_Sample, bg = 'white', width=20, height=10,
                       text = 'Click any colored button \n to start')
sampleColor.pack()
frm_Sample.grid(row=5, rowspan=2, column=4, columnspan=2)


 




window.mainloop()
