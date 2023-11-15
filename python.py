import ipinfo
access_token = 'a96089d80d0f09'
handler = ipinfo.getHandler(access_token)
ip_adress = 'ip_adress'
details = handler.getDetails(ip_adress)
details.city