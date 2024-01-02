"""
ips validos vão de 0.0.0.0 até 255.255.255.255
"""

import re, itertools, functools

#[0-1][0-9]{2}\.(?:[0-1][0-9]{2}|[2][0-4][0-9]|[2][5][0-5])
regexp = re.compile(r"""
    ^
   (?:
     (?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.?          
   ){4} 
    \b
    $
""", flags=re.X)

ipv4 = itertools.product(range(256), repeat=4)
print('.'.join(map(str, list(next(ipv4)))))
        
for ip in range(301):
    ipfake = f'{ip}.'*4
    ipfake = ipfake.strip('.')
    
    print(ipfake, regexp.findall(ipfake))
