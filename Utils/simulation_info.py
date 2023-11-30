import Lib.Har as ht
from datetime import datetime
work_dir = r'C:\Perf\cma-perf\gatling-bundle\results'
simu_file =  work_dir + '\\static_simulation.log'

ht.get_start_end(simu_file)

with open(simu_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.find('RUN') >= 0:
            continue
        infos = line.split('\t')
        start = str(datetime.utcfromtimestamp(int(infos[3]) / 1000))[0:19]
        end=''
        if line.find('USER') <0:
            end = str(datetime.utcfromtimestamp(int(infos[4]) / 1000))[0:19]
        print(start, ";", end)


