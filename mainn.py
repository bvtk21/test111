import socket
import geoip2.database

# Получаем IP-адрес устройства
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("IP-адрес устройства:", ip_address)

# Определяем страну по IP-адресу
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
response = reader.country(ip_address)
print("Страна устройства:", response.country.name)