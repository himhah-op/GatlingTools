#!C:\Apps\Python310 python
# encoding: utf8
import json
from urllib.parse import urlparse
from haralyzer import HarParser, HarPage
import os
from datetime import datetime


def get_domains (har_file):
    domains=[]
    with open(har_file, encoding="utf8") as f:
        har_parser = HarParser(json.loads(f.read()))
        for page in har_parser.pages:
            for entry in page.entries:
                domain = urlparse(entry.url).netloc
                if domain not in domains:
                    domains.append(domain)
    return (domains)

def get_content_types (har_file):
    content_types=[]
    with open(har_file, encoding="utf8") as f:
        har_parser = HarParser(json.loads(f.read()))
        for page in har_parser.pages:
            for entry in page.entries:
                if entry.response.contentType not in content_types:
                    content_types.append(entry.response.contentType)
    return (content_types)

def get_urls (har_file, filter):
    with open(har_file, encoding="utf8") as f:
        har_parser = HarParser(json.loads(f.read()))
        for page in har_parser.pages:
            for entry in page.entries:
                domain = urlparse(entry.url).netloc
                if domain in filter or len(filter)==0:
                    print (entry.request.method, entry.url, entry.response.contentType)

def get_correlation (har_file, value):
    with open(har_file, encoding="utf8") as f:
        har_parser = HarParser(json.loads(f.read()))
        for page in har_parser.pages:
            for entry in page.entries:
                filtred = []
                if entry.response.contentType is None:
                    continue
                if entry.response.status in [301, 302, 0]:
                    continue
                if entry.response.contentType.find("text") >= 0 or \
                        entry.response.contentType.find("json") >= 0 or \
                        entry.response.contentType.find("javascript") >= 0 or \
                        entry.response.contentType.find("json") >= 0:
                    resp = entry.response
                    try:
                        content = resp.text
                    except:
                        print("ERROR reading :", entry.url)
                        continue
                    content = content.replace('\n', ' ')
                    content = content.replace('\r\n', ' ')
                    index = content.find(value)
                    if index >= 0:
                        print("====>", entry.request.method, "   ", entry.url)
                        print("====>", entry.response.contentType)
                        start = max(0, index - 40)
                        end = min(index + 200, len(content))
                        print("====>", content[start:end])
                else:
                    filtred.append(entry.response.contentType)

def filter_content_types (har_file, new_har_file, filter):
    filtred_content = []
    accepted_content = []
    with open(har_file, encoding="utf8") as f:
        jsonContent = json.loads(f.read())
        entries = []

        for entrie in jsonContent['log']['entries']:
            content_type = entrie['response']['content']['mimeType'].split('/')
            if content_type[0] in filter or content_type[1].split(';')[0] in filter or len(filter)==0:
                if content_type not in accepted_content:
                    accepted_content.append(content_type)
                entries.append(entrie)
            else:
                if content_type not in filtred_content and len(filter)>0:
                    filtred_content.append(content_type)
        jsonContent['log']['entries'] = entries
    with open(new_har_file, "w", encoding="utf8") as outfile:
        json.dump(jsonContent, outfile)
    print('Accepted')
    for filter in accepted_content:
        print(filter)
    print('\n\nFiltred')
    for filter in filtred_content:
        print(filter)

def filter_domains (har_file, new_har_file, filter):
    with open(har_file, encoding="utf8") as f:
        jsonContent = json.loads(f.read())
        entries = []
        filtred_domains = []
        accepted_domains = []

        for entrie in jsonContent['log']['entries']:
            domain = urlparse(entrie['request']['url']).netloc
            if domain in filter or len(filter)==0:
                if domain not in accepted_domains:
                    accepted_domains.append(domain)
                entries.append(entrie)
            else:
                if domain not in filtred_domains and len(filter)>0:
                    filtred_domains.append(domain)
        jsonContent['log']['entries'] = entries
    with open(new_har_file, "w", encoding="utf8") as outfile:
        json.dump(jsonContent, outfile)
    print('Accepted')
    for filter in accepted_domains:
        print(filter)
    print('\n\nFiltred')
    for filter in filtred_domains:
        print(filter)

def find_param_to_correlate (entry, keys):
    found = ""
    for key in keys:
        for param in entry.request.queryString:
            if param['name'].find(key)>=0:
                found=("QueryString", param['name'])
                break
        if entry.request.text is not None:
            if entry.request.text.find(key)>=0:
                found=("Body", entry.request.text)
                break
        for header in entry.request.headers:
            if header['name'].find(key) >=0 or header['value'].find(key)>=0:
                found=("Header", header)
                break
    return (found)

def find_correlation (har_file, keys):
    with open(har_file, encoding="utf8") as f:
        har_parser = HarParser(json.loads(f.read()))
        for page in har_parser.pages:
            for entry in page.entries:
                found = find_param_to_correlate(entry, keys)
                if found != "":
                    print (entry.request.url)
                    if found[0]=='QueryString':
                        print('QueryString  ', found[1])
                    if found[0]=='Body':
                        print('Body  ' , found[1])
                    if found[0]=='Header':
                        print('Header  ' , found[1])