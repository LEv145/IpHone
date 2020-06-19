import requests

class Ip():
    def __init__(self, ip):
        self._ip = ip
    def get_ip(self):
        response      = requests.get(f'http://ipinfo.io/{self._ip}/json')
        try:
            user_ip       = response.json()['ip']
        except:
            user_ip = "Не найдено"
        try:
            user_city     = response.json()['city']
        except:
            user_city = "Не найдено"
        try:
            user_region   = response.json()['region']
        except:
            user_region = "Не найдено"
        try:
            user_country  = response.json()['country']
        except:
            user_country = "Не найдено"
        try:
            user_loc      = response.json()['loc']
        except:
            user_loc = "Не найдено"
        try:
            user_org      = response.json()['org']
        except:
            user_org = "Не найдено"
        try:
            user_timezone = response.json()['timezone']
        except:
            user_timezone = "Не найдено"


        print(f"""
    [INFORMATION ABOUT IP: {user_ip}]
    ===================================
    CITY: {user_city}
    REGION: {user_region}
    COUNTRY: {user_country}
    LOCATION: {user_loc}
    TIMEZONE: {user_timezone}""")

class Phone():
    def __init__(self, phone):
        self._phone = phone
    def get_phone(self):
        response            = requests.get(f'https://htmlweb.ru/geo/api.php?json&telcod={self._phone}')

        try:
            user_city           = response.json()['capital']['english']
        except:
            user_city = "Не найдено"
        try:
            user_region         = response.json()['country']['id']
        except:
            user_region = "Не найдено"
        try:
            user_country        = response.json()['country']['english']
        except:
            user_country = "Не найдено"
        try:
            user_w, user_h      = response.json()['capital']['latitude'], response.json()['capital']['longitude']
        except:
            user_w, user_h = "Не найдено"
        try:
            user_post           = response.json()['capital']['post']
        except:
            user_post = "Не найдено"
        try:
            user_operator       = response.json()['0']['oper']
        except:
            user_operator = "Не найдено"


        print(f"""
    [INFORMATION ABOUT PHONE: {self._phone}]
    ===================================
    CITY: {user_city}
    REGION: {user_region}
    COUNTRY: {user_country}
    LOCATION: {user_w} {user_h}
    """)
