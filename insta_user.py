import requests
import random

print(' @hd0r3 - @baqertools')
print('\n')
user = 'qwertyuiopasdfghjklzxcvbnm1234567890'
zok=0
def zz():
 global zok
 while True:
 	try:
	 	us = str("".join(random.choice(user)for x in range(1)))
	 	um = str("".join(random.choice(user)for x in range(1)))
	 	ur = str("".join(random.choice(user)for x in range(1)))
	 	usery= us+us+'.'+um+ur
	 	url = 'https://i.instagram.com/api/v1/accounts/create/'
	 	he = {
	'Content-Length': '437',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
	'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
	'Cookie2': '$Version=1',
	'Accept-Language': 'en-IQ, en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'Accept-Encoding': 'gzip',}
		
	 	from uuid import uuid4
	 	da = {
	 	"email":"zodhok@gmail.com",
	 	"username":f"{usery}",
	 	"password":"zxcvbm1@"+usery,
	 	"device_id":"android-"+str(uuid4()),
	 	"guid":str(uuid4()),
	 	}		
	 	rr = requests.post(url,headers=he,data=da).text
	 	#print(rr)
	 	#exit()
	 	if "username" in rr:
	 		zok+=1
	 		print(f' {zok} : Bad User : {usery}')
	 	elif 'email_is_taken' in rr:
	 		
	 		zok+=1
	 		print(rr)
	 		print(f' {zok} : Good User : {usery}')
	 		tlg=f'''
✅User Insta
----------------------------
user : {usery}
---------------------------
By :  @hd0r3 - @baqertools
	'''
	 		requests.post(f"https://api.telegram.org/bot6258466831:AAHYyJr_BADJmnx2AD1bYfAF9jPQpTGAinY/sendMessage?chat_id=1214392661&text="+str(tlg))
	 	else:
	 		zok+=1
	 		print(f' {zok} : Bad User : {usery}')
 		
 	except:
 		zz()
 
while True:
	zz()
