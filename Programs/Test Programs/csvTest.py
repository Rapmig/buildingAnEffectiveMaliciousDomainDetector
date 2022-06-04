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

ans = {'Domain Name' : [],'cons' : [],'active' : [],'life' : [],'averageTTL' : []}
ansArray = []
with open('benign_domains.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        updatedBool = False
        lifetimeBool = False
        print(row[0])
        website = row[0]

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

        #print(socket.gethostbyaddr('8.8.8.8')[0])
        try:
            w = whois.query(website)
        except Exception:
            #ans.update({'Domain Name' : website,'cons' : amountOfConsecutiveCharacters,'active' : "none",'life' : "none",'averageTTL' : "none"})
            line_count += 1
            continue
        #w.expiration_date  # dates converted to datetime object
        #w.text  # the content downloaded from whois server 
        #print(w)  # print values of all found attributes 
        #print(w.creation_date)
        #print(w.expiration_date)
        #print(w.updated_date)
        if(w is None):
            line_count += 1
            continue
        try:
            creationDate = w.creation_date
            if(isinstance(creationDate,list)):
                creationDate = creationDate[0].date()
            else:
                creationDate = creationDate.date()
            expirationDate = w.expiration_date
            if(isinstance(expirationDate,list)):
                expirationDate = expirationDate[0].date()
            else:
                expirationDate = expirationDate.date()
            updatedDate = w.last_updated
            if(isinstance(updatedDate,list)):
                updatedDate = updatedDate[0].date()
            else:
                updatedDate = updatedDate.date()
            #print(creationDate)
            #print(expirationDate)
        except Exception:
            line_count += 1
            continue
        

        if(isinstance(updatedDate,datetime.date) and isinstance(creationDate,datetime.date)):
            updatedBool = True
            activeTimeDomain = (updatedDate-creationDate)
            activeTimeDomainOutput =  activeTimeDomain.days/365.25
            #print(activeTimeDomainOutput, "years")
        else:
            #activeTimeDomainOutput = "none"
            line_count += 1
            continue
        if(isinstance(expirationDate,datetime.date) and isinstance(creationDate,datetime.date)):
            lifetimeBool = True  
            lifeTimeDomain = (expirationDate-creationDate)
            lifeTimeDomainOutput = lifeTimeDomain.days/365.25
            #print(lifeTimeDomainOutput, "years")
        else:
            #lifeTimeDomainOutput = "none"
            line_count += 1
            continue


        p = subprocess.Popen(["ping",'-c 20',website], stdout=subprocess.PIPE)
        res=p.communicate()[0]
        if p.returncode > 0:
            #print('server error')
            averageTTL = "none"
            continue
        else:
            pattern = re.compile('ttl=\d*')
            #print(pattern.search(str(res)).group())
            averageTTL = ''.join(x for x in pattern.search(str(res)).group() if x.isdigit())
            #print (averageTTL)
    
        ans.update({'Domain Name' : website,'cons' : amountOfConsecutiveCharacters,'active' : activeTimeDomainOutput,'life' : lifeTimeDomainOutput,'averageTTL' : averageTTL})
        #print(ans)
        ansArray.append(ans.copy())
        #print(ansArray)
        line_count += 1
        
        #print(f'Processed {line_count} lines.')
    print(ansArray)


fields = {'Domain Name', 'cons', 'active', 'life', 'averageTTL'}
with open('benign_domainsOUTPUT.csv', mode='w') as output_file:
    writer = csv.DictWriter(output_file, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    writer.writerows(ansArray) 