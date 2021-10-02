import sequence_pb2
import os
from termcolor import colored as col
from time import process_time
import google.protobuf.text_format
from tkinter import filedialog
from tkinter import *
tk = Tk()
tk.withdraw()


def parsesequence(sequencedir):
    currentname = os.path.basename(sequencedir)
    print(col('Found Sequence:', 'cyan'), col(currentname, 'magenta'))
    f = open(sequencedir, 'r')
    currentout = open('./converted/' + currentname + '.sequence', 'wb')
    # thank you so much for doute#7958 on the Python help discord for help with this code
    sequence = google.protobuf.text_format.Parse(f.read(), sequence_pb2.Sequence())
    currentout.write(sequence.SerializeToString())
    f.close()
    currentout.close()
    stoptime = process_time()
    print(col('Processed', 'cyan'),
          col(currentname, 'magenta') +
          col('!', 'cyan'),
          col('(Time Elapsed:', 'cyan'),
          col(stoptime, 'magenta'),
          col('seconds)', 'cyan'))
    print(col('Output:', 'cyan'), col(currentname + '.sequence', 'magenta'))


parsesequence(filedialog.askopenfilename(filetypes=[('Text files', '*.txt')]))
