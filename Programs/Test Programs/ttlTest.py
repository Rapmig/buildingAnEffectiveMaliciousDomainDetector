import subprocess
import re
p = subprocess.Popen(["ping","www.google.com"], stdout=subprocess.PIPE)
res=p.communicate()[0]
if p.returncode > 0:
    print('server error')
else:
    pattern = re.compile('TTL=\d*')
    print(pattern.search(str(res)).group())