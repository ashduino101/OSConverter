import sequence_pb2
import os
from termcolor import colored as col
from time import process_time
from tkinter import filedialog
from tkinter import *
tk = Tk()
tk.withdraw()


def parsesequence(sequencedir):
    currentname = os.path.basename(sequencedir)
    print(col('Found Sequence:', 'cyan'), col(currentname, 'magenta'))
    currentout = open('./converted/' + currentname + '.sequence', 'w+')
    f = open(sequencedir, 'rb')
    sequence = sequence_pb2.Sequence()
    sequence.ParseFromString(f.read())
    currentout.write(str(sequence))
    f.close()
    currentout.close()
    stoptime = process_time()
    print(col('Processed', 'cyan'),
          col(currentname, 'magenta') +
          col('!', 'cyan'),
          col('(Time Elapsed:', 'cyan'),
          col(stoptime, 'magenta'),
          col('seconds)', 'cyan'))
    print(col('Output:', 'cyan'), col(currentname + '.txt', 'magenta'))


parsesequence(filedialog.askopenfilename(filetypes=[('Binary sequences', '*.sequence')]))
