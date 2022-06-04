import csv
from multiprocessing.connection import answer_challenge
import whois
import datetime
import dns.resolver
import socket
import subprocess
import re
from itertools import groupby
import csv
from collections import defaultdict


ans = [{'Domain Name': 'amazon.com', 'cons': 1, 'active': 24.511978097193705, 'life': 29.9958932238193, 'averageTTL': '219'}, {'Domain Name': 'google.com', 'cons': 2, 'active': 21.982203969883642, 'life': 30.99520876112252, 'averageTTL': '116'}, {'Domain Name': 'facebook.com', 'cons': 1, 'active': 24.829568788501028, 'life': 34.001368925393564, 'averageTTL': '55'}, {'Domain Name': 'youtube.com', 'cons': 1, 'active': 16.91170431211499, 'life': 17.998631074606433, 'averageTTL': '116'}, {'Domain Name': 'twitter.com', 'cons': 1, 'active': 21.99041752224504, 'life': 23.000684462696782, 'averageTTL': '51'}, {'Domain Name': 'boy.co.jp', 'cons': 1, 'active': 25.018480492813143, 'life': 26.015058179329227, 'averageTTL': 'none'}]
fields = {'Domain Name', 'cons', 'active', 'life', 'averageTTL'}
with open('benign_domainsTESTOUTPUT.csv', mode='w') as output_file:
    writer = csv.DictWriter(output_file, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    writer.writerows(ans) 