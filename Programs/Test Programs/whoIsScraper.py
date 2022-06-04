import whois
from ipwhois import IPWhois
import datetime
import dns.resolver
import socket
import subprocess
import re
from itertools import groupby
import csv
from datetime import datetime, timezone

website = 'twitter.com'

#Consecutive Characters Checker
groups = groupby(website)
result = [(label, sum(1 for _ in group)) for label, group in groups]
#print(result)
i = 0
counter = 0
mostConsecutive = 0
for x,y in result:
    if int(y) > i:
        i = y
        mostConsecutive = counter
    
    counter =+1

amountOfConsecutiveCharacters = result[mostConsecutive][1]   
#print(result[mostConsecutive])
#print(result[mostConsecutive][1])

#NOT WORKING
#obj = IPWhois(website)
#print(obj)
#res = obj.lookup()
#print(res)

#print(socket.gethostbyaddr('8.8.8.8')[0])
w = whois.query(website)
#w.expiration_date  # dates converted to datetime object
#w.text  # the content downloaded from whois server 
print (w)  # print values of all found attributes 
creationDate = w.creation_date
if(isinstance(creationDate,list)):
    creationDate = creationDate[0].replace(tzinfo=None)
expirationDate = w.expiration_date
if(isinstance(expirationDate,list)):
    expirationDate = expirationDate[0].replace(tzinfo=None)
updatedDate = w.last_updated
if(isinstance(updatedDate,list)):
    updatedDate = updatedDate[0].replace(tzinfo=None)
if(updatedDate == "None" or updatedDate):
    updatedBool = True
    if (isinstance(updatedDate,list) and isinstance(creationDate,list)):
        activeTimeDomain = (updatedDate[0]-creationDate[0])
    elif (isinstance(updatedDate,list)):
        activeTimeDomain = (updatedDate[0]-creationDate)
    elif (isinstance(creationDate,list)):
        activeTimeDomain = (updatedDate-creationDate[0])
    else:
        activeTimeDomain = (updatedDate-creationDate)
    activeTimeDomainOutput =  activeTimeDomain.days/365.25
    #print(activeTimeDomainOutput, "years")
if(w.expiration_date == "None" or w.expiration_date):
    lifetimeBool = True  
    if (isinstance(expirationDate,list) and isinstance(creationDate,list)):
        lifeTimeDomain = (expirationDate[0]-creationDate[0])
    elif (isinstance(expirationDate,list)):
        lifeTimeDomain = (expirationDate[0]-creationDate)
    elif (isinstance(creationDate,list)):
        lifeTimeDomain = (expirationDate-creationDate[0])
    else:
        lifeTimeDomain = (expirationDate-creationDate)
    lifeTimeDomainOutput = lifeTimeDomain.days/365.25
    #print(lifeTimeDomainOutput, "years")




#Active Time Of Domain In Years

#Lifetime of Domain In Years


#print("BEFORE IF Line 23")
p = subprocess.Popen(["ping",'-c 20',website], stdout=subprocess.PIPE)
#print("BEFORE IF Line 24")
res=p.communicate()[0]
#print("BEFORE IF Line 25")
if p.returncode > 0:
    print('server error')
else:
    pattern = re.compile('ttl=\d*')
    #print(pattern.search(str(res)).group())
    averageTTL = ''.join(x for x in pattern.search(str(res)).group() if x.isdigit())
    print (averageTTL)


