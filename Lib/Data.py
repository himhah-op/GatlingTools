import csv
from random import randrange
import glob
import os

separator=','

def check_csv_file(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if len(row['access_code']) != 9:
                print ("Error access_code lenght. Row : ", line_count, row['access_code'])
                break
            if len(row['personne']) != 8:
                print ("Error personne lenght. Row : ", line_count, row['personne'])
                break
            line_count+=1
    print (line_count)

def pad_line_carte (line):
    data = line.split(separator)
    if len(data)>1:
        return ('{0}{2}{1}\n'.format(str(data[0].zfill(9)), separator, data[1]))
    else:
        return (str(data[0].zfill(9)) + '\n')

def pad_line (line):
    data = line.split(separator)
    if len(data)>1:
        return ('{0},{1},{2}\n'.format(str(data[0].zfill(9)), str(data[1].zfill(8)), data[2]))
    else:
        return (str(data[0].zfill(9)) + '\n')

def pad_line_carte_credit (line):
    data = line.split(separator)
    if len(data)>1:
        return ('{0},{1},{2},{3}\n'.format(str(data[0].zfill(9)), str(data[1].zfill(8)), data[2], data[3]))
    else:
        return (str(data[0].zfill(9)) + '\n')

def pad_csv_columns (csv_file):
    separator = ','
    access = open(csv_file, 'r')
    access_padded = open(csv_file + '.padded', 'w')
    count = 0
    while True:
        line = access.readline().replace('\n', '').replace('"', '').strip()
        data = line.split(separator)
        if not line:
            break
        access_padded.write(pad_line(line))
    access_padded.close()
    access.close()

def split_file (file_in, file1, file2):
    file_full = open(file_in, 'r')
    file_part1 = open(file1 , 'w')
    file_part2 = open(file2 , 'w')
    lines = file_full.readlines()
    total_rows = len(lines)
    file_part1.write(lines[0])
    file_part2.write(lines[0])
    for i in range (1, int(total_rows/2)):
        line = lines[i]
        file_part1.write(line)
    for i in range (int(total_rows/2)+1, total_rows):
        line = lines[i]
        file_part2.write(line)
    print (file_in, total_rows)
    file_part1.close()
    file_part2.close()
    file_full.close()

def random_data_file (file_in, file_out, count):
    file_full = open(file_in, 'r')
    file_random = open(file_out, 'w')
    lines = file_full.readlines()
    total_rows = len(lines)
    file_random.write(lines[0])
    for i in range (1, count):
        line = lines[randrange(total_rows-1)+1]
        file_random.write(line)
    file_random.close()
    file_full.close()


def split_all_csv_files(work_dir):
    os.chdir(work_dir+'\\full')
    csv_files = glob.glob('*.csv')
    for csv_file in csv_files:
        print (csv_file)
        split_file(csv_file, work_dir+'\\part1\\'+csv_file,  work_dir+'\\part2\\'+csv_file )
