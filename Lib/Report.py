#!C:\Apps\Python310 python
# encoding: utf8
from datetime import datetime
import os

def get_start_end (simu_file):
    print (simu_file)
    with open(simu_file, 'r') as file:
        lines = file.readlines()
        infos = lines[0].split('\t')
        start = str(datetime.utcfromtimestamp(int(infos[3])/1000))[0:16]
        infos = lines[-2].split('\t')
        end = str(datetime.utcfromtimestamp(int(infos[3])/1000))[0:16]
        print (start, "========", end)

def get_all_sim_info (work_dir):
    all_files = os.listdir(work_dir)
    log_files = [file for file in all_files if file.endswith('.log')]
    for log_file in log_files:
        get_start_end(work_dir + '\\' + log_file)

def filter_report(sim_log_in, sim_log_out, start, end):
    start =  datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end =  datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    start = int(start.timestamp()*1000)
    end = int(end.timestamp()*1000)
    result_file = open(sim_log_in, 'r')
    filtred_file = open(sim_log_out, 'w')
    count = 0
    while True:
        line = result_file.readline().replace('\n', '').replace('"', '').strip()
        data = line.split("\t")
        if (data[0] == 'ERROR'):
            ts =  int(data[2])
        else:
            ts = int(data[3])
        if ts < start:
            continue
        if ts > end:
            break
        if not line:
            break
        filtred_file.write((line+'\n'))
        count+=1
    result_file.close()
    filtred_file.close()
