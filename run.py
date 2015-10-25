# -*- coding: utf-8 -*-

import sys
import os
import csv
import re
import glob
from settings import *

def read_txt():
    for filename in glob.glob(os.path.join(SOURCE_PATH)):
        with open(filename, 'r') as txt:
            reader = csv.reader(txt, delimiter=SOURCE_DELIMITER, quotechar='"')
            for row in reader:
                yield row

def write_csv(wrangle=True):
    with open(OUTPUT_PATH, 'wb') as output:
        writer = csv.writer(output, delimiter=OUTPUT_DELIMITER, quotechar='"')

        if wrangle:
            writer.writerow(OUTPUT_HEADER)
            for row in read_txt():
                writer.writerow(wrangle_row(row))
        else:
            writer.writerow(SOURCE_HEADER)
            for row in read_txt():
                writer.writerow([encode(item) for item in row])

def wrangle_row(row):
    addr_old = "%s %s %s %s %d-%d %s" % (row[1].strip(), row[2].strip(), row[3].strip(), row[18].strip() if row[18] else row[4].strip(), int(row[6].strip()), int(row[7].strip()), row[25].strip())
    addr_new = "%s %s %s %d-%d %s" % (row[1].strip(), row[2].strip(), row[9].strip(), int(row[11].strip()), int(row[12].strip()), row[25].strip())
    postal_code = int(row[19])

    # remove more than at least 2 spaces between words
    addr_old = encode(' '.join(re.split(r'\{2,}', addr_old)))
    addr_new = ' '.join(re.split(r'\{2,}', encode(addr_new)))

    return [postal_code, addr_old, addr_new]

def encode(s):
    if isinstance(s, unicode):
        s = s.encode(OUTPUT_ENCODING)
    elif not isinstance(s, str):
        s = str(s)
    else:
        s = unicode(str(s), SOURCE_ENCODING).encode(OUTPUT_ENCODING)
    return s

if __name__ == "__main__":
    print'''
    converting <*.txt> to <addresses.csv> ...
    '''

    write_csv()
