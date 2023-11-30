#!C:\Apps\Python310 python
# encoding: utf8
import os
from urllib.parse import urlparse
import Lib.Simulation as sim
import config

java_file = config.work_dir + '\\orangehrm.java.initial'
java_file_renamed = config.work_dir + '\\orangehrm.java.renamed'
#a revoir
# duplicates = sim.find_duplicate_ressources (java_file)
# print (duplicates)
# sim.comment_duplicate_ressources (sim_file)
sim.rename_queries (java_file, java_file_renamed)
