#!C:\Apps\Python310 python
# encoding: utf8
import Lib.Har as ht
from urllib.parse import urlparse
from haralyzer import HarParser, HarPage

import config

har_file = config.work_dir + '\\' + config.har_file
har_file_filtred = config.work_dir + '\\' + config.har_filtred
token = '30'
# mercure_token / access_token / connection_id / client_id / secret

# Etape 1 : liste des domaines utilisés
print (ht.get_domains (har_file))
# Etape 2 : Filtrer sur les domaines utilisés
# ht.filter_domains (har_file, new_har_file, ['opensource-demo.orangehrmlive.com'])

# Etape 3 : liste des content types
# content_types = ht.get_content_types(har_file)
# for content_type in content_types:
#    print(content_type)

# Etape 4 : filtre  des content types
# ht.filter_content_types(har_file, har_file_filtred, ['html', 'json', 'xml'])

# Etape 5 : lister les URLs appelées
#ht.get_urls (har_file_filtred, [])

# Etape 6 : Recherche des données à correler
# ht.find_correlation (har_file_filtred, config.keys)

# Etape 7 : Recherche des requetes dont les réponses contiennent les données à correlér
ht.get_correlation(har_file_filtred, "ad70.A63KDR6jt9j9VHbuPp-QVjPgR_PbPgrs1DIYSLajwNI.dNqJS07p_a26HB-Ed_v5LACSMbv2anyAi1VPENThlb5clf5MR9b8uq5mQg")
