import requests


def ip(_ip):
	response      = requests.get(f'http://ipinfo.io/{_ip}/json')

	user_ip       = response.json()['ip']
	user_city     = response.json()['city']
	user_region   = response.json()['region']
	user_country  = response.json()['country']
	user_loc      = response.json()['loc']
	user_org      = response.json()['org']
	user_timezone = response.json()['timezone']

	print(f"""
[INFORMATION ABOUT IP: {user_ip}]
===================================
CITY: {user_city}
REGION: {user_region}
COUNTRY: {user_country}
LOCATION: {user_loc}
TIMEZONE: {user_timezone}""")


def phone(_phone):
	response            = requests.get(f'https://htmlweb.ru/geo/api.php?json&telcod={_phone}')

	user_city           = response.json()['capital']['english']
	user_region         = response.json()['country']['id']
	user_country        = response.json()['country']['english']
	user_w, user_h      = response.json()['capital']['latitude'], response.json()['capital']['longitude']
	user_post           = response.json()['capital']['post']
	user_operator       = response.json()['0']['oper']

	print(f"""
[INFORMATION ABOUT PHONE: {_phone}]
===================================
CITY: {user_city}
REGION: {user_region}
COUNTRY: {user_country}
LOCATION: {user_w} {user_h}
OPERATOR: {user_operator}""")