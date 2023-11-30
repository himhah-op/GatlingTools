#!C:\Apps\Python310 python
# encoding: utf8
import os
from urllib.parse import urlparse
def get_name (next_line, index):
    next_line = next_line.replace('(', '').replace(')', '').replace('"', '').replace('\r\n', '').replace('\n', '')
    if next_line.find('?')>0:
        next_line=next_line[0:next_line.find('?')]
    parts = next_line.split('/')
    if len(parts)==2:
        if parts[1].find('.')>0:
            name = parts[1]
        else:
            name = "Home"
    else:
        if len(parts)>1:
            name = parts[len(parts)-2] + '/' + parts[len(parts)-1]
        else:
            name = parts[len(parts)-1]
    name = str(index).zfill(3) + ':GET ' + name.replace('#', '').replace('{', '').replace('}', '')
    return (name)

def comment_duplicate_ressources(sim_file):
    simu = open(sim_file, 'r')
    i=0
    lines = simu.readlines()
    index=0
    urls=[]
    ressources=[]
    while i<len(lines):
        line = lines[i]
        line = line.replace('\r\n', '').replace('\n', '')
        if line.find('.get("')>=0:
            url = line.split('"')[1]
            url = url.replace('#', '').replace('{', '').replace('}', '')
            a = urlparse(url)
            if url in urls or os.path.basename(a.path) in ressources:
                print ("//" + line)
            else:
                print(line)
            urls.append(a.path)
            ressources.append(os.path.basename(a.path))
            index+=1
        else:
            print(line)
        i+=1
    simu.close()

# TODO : A revoir. Fonctionne uniquement sur les ressources statiques.
def find_duplicate_ressources(sim_file):
    simu = open(sim_file, 'r')
    i=0
    lines = simu.readlines()
    index=0
    urls=[]
    ressources=[]
    duplicates=[]
    while i<len(lines):
        line = lines[i]
        line = line.replace('\r\n', '').replace('\n', '')
        if line.find('.get("')>=0 or line.find('.post("')>=0:
            url = line.split('"')[1]
            url = url.replace('#', '').replace('{', '').replace('}', '')
            a = urlparse(url)
            if url in urls:
                if url not in duplicates:
                    duplicates.append(url)
#            if os.path.basename(a.path) in ressources:
#                if os.path.basename(a.path) not in duplicates:
#                    duplicates.append(os.path.basename(a.path))
            urls.append(a.path)
            ressources.append(os.path.basename(a.path))
            index+=1
        i+=1
    simu.close()
    return (duplicates)

def rename_queries (sim_file, new_sim_file):
    simu = open(sim_file, 'r')
    new_simu = open(new_sim_file, 'w')
    i=0
    lines = simu.readlines()
    index=0
    while i<len(lines):
        line = lines[i]
        if i<len(lines)-1:
            next_line = lines[i+1]
        else:
            next_line=''
        if line.find('http("')>=0:
            name = get_name (next_line, index)
            line = line.replace('\r\n', '').replace('\n', '')
            parts = line.split('"')
            new_line = '{0}"{1}"{2}'.format(parts[0], name, parts[2])
            print (new_line)
            new_simu.write(new_line +  '\n')
            index+=1
        else:
            new_simu.write(line)
        i+=1
    simu.close()
