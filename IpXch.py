#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import os
import time
import random

class Colors:
    RED = "\033[31;1m"
    GREEN = "\033[32;1m"
    YELLOW = "\033[33;1m"
    BLUE = "\033[34;1m"
    MAGENTA = "\033[35;1m"
    CYAN = "\033[36;1m"
    RESET = "\033[0m"

def colored_text(text, color):
    return f"{color}{text}{Colors.RESET}"

def random_color():
    color_list = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
    return random.choice(color_list)

os.system("clear")
logo = colored_text('''
             uu$:$:$:$:$:$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
         u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$*   *$$$*   *$$$$$$u
       *$$$$*      u$u       $$$$*
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         *$$$$uu$$$   $$$uu$$$$*
          *$$$$$$$*   *$$$$$$$*
            u$$$$$$$u$$$$$$$u
             u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$u$u$u$u$u$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$**
     $$$*    ___________________  $$$$*
            |Made by: Cutehacker|
            |___________________|
            | PIXRO Version: v1 |
            |___________________|
''', random_color())

# Rest of the code remains unchanged.
def per():
  api2 = f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  time.sleep(1)

  data = requests.get(api2).json()
  ##-----------Query---------##
  print("\n[~] [IP]:", data['query'])
  ##--------------ISP-----------
  print("[~] [ISP] :", data['isp'])
  if data['isp'] == False:
    print('[~] [ISP no encontrado!]')
  ##------------Org-----------##
  print("[~] [Organizacion]:", data['org'])
  if data['org'] == False:
    print('[~] [Organizacion no encontrado!]')
  ##-----------City---------##
  print("[~] [city]:", data['city'])
  if data['city'] == False:
    print('[~] [Ciudad no encontrada!]')
  ##-----------Country---------##
  print("[~] [country]:", data['country'])
  if data['country'] == False:
    print('[~] [Nombre del pais no encontrado!]')
  ##----------Region-------##
  print("[~] [Region]:", data['region'])
  if data['region'] == False:
    print('[~] [Region no encontrada!]')
  ##---------Nombre del continente---
  print("[~] [Nombre del continente]:", data['continent'])
  if data['country'] == False:
    print('[~] [Nombre del continente no encontrado!]')
  #-----------Región / estado-------##
  print("[~] [Región / estado]:", data['regionName'])
  if data['regionName'] == False:
    print('[~] [Region / Estado no encontrado!]')
  ##----------2 letras continente##---
  print("[~] [Código de continente de dos letras]:", data['continentCode'])
  if data['country'] == False:
    print('[~] [Código de continente de dos letras no encontrado!]')
  #---Latitud----##
  print("[~] [Latitud]:", data['lat'])
  if data['lat'] == False:
    print('[~] [Latitud no encontrada!]')
  ##----------Longitud------##
  print("[~] [Longitud]:", data['lon'])
  if data['lon'] == False:
    print('[~] [Longitud no encontrada!]')
  ##--------------Timezone---------##
  print("[~] [Zona horaria]:", data['timezone'])
  if data['timezone'] == False:
    print('[~] [Zona horaria no encontrada!]')
  ##-------------- ZIP--------------##
  print("[~] [Codigo zip]:", data['zip'])
  if data['zip'] == False:
    print('[~] [Codigo zip no encontrado!]')
  ##------------ AS -------------------##
  print("[~] [AS número y organización]:", data['as'])
  if data['as'] == False:
    print('[~] [AS número y organización no encontrado!]')
  ##-----------Countrycode-----##
  print("[~] [Código de país de dos letras]:", data['countryCode'])
  if data['countryCode'] == False:
    print('[~] [Código de país de dos letras no encontrado!]')
  ##-----------Reverse IP---------##
  print("[~] [DNS inverso de la IP]: ", data['reverse'])
  if data['reverse'] == False:
    print('[~] [DNS inverso de la IP!]')
  ##--------------Mobile------##
  print("[~] [Conexión móvil (celular)]:", data['mobile'])
  if data['mobile'] == False:
    print('[~] [Conexión móvil no encontrado!]')
  #----currency----##
  print('[~] [Moneda nacional]:', data['currency'])
  if data['currency'] == False:
    print('[~] [Moneda nacional no encontrada!]')
  #-----district----#
  print('[~] [Distrito (subdivisión de la city)]:', data['district'])
  if data['district'] == False:
    print('[~] [Distrito no encontrado!]')
  #-------Proxy-----#
  print('[~] [Proxy, VPN o Tor]:', data['proxy'])
  if data['proxy'] == False:
    print('[~] [Proxy, VPN o Tor no encontrado!]')

def locate():
  print('\n[~] ENTER THE IP OF VICTIM')
  ipin = input('[~] IP: ')
  print(f'[~] FINDING DETAILS FOR: {ipin}')
  time.sleep(1)
  api = f"http://ip-api.com/json/{ipin}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  data = requests.get(api).json()
  ##-----------Query---------##
  print("\n[~] [IP De la victima]:", data['query'])
  ##--------------ISP-----------
  try:
    print("[~] [ISP] :", data['isp'])
    if data['isp'] == False:
      print('[~] [ISP no encontrado!]')
  ##------------Org-----------##
    print("[~] [Organizacion]:", data['org'])
    if data['org'] == False:
     print('[~] [Organizacion no encontrado!]')
  ##-----------City---------##
    print("[~] [City]:", data['city'])
    if data['city'] == False:
     print('[~] [Ciudad no encontrada!]')
  ##-----------Country---------##
    print("[~] [COUNTRY ]:", data['country'])
    if data['country'] == False:
     print('[~] [Nombre del pais no encontrado!]')
  ##----------Region-------##
    print("[~] [Region]:", data['region'])
    if data['region'] == False:
     print('[~] [Region no encontrada!]')
  ##---------Nombre del continente---
    print("[~] [COUNTRY]:", data['continent'])
    if data['country'] == False:
     print('[~] [Nombre del continente no encontrado!]')
  #-----------Región / estado-------##
    print("[~] [Región / estado]:", data['regionName'])
    if data['regionName'] == False:
      print('[~] [Region / Estado no encontrado!]')
  ##----------2 letras continente##---
    print("[~] [Código de continente de dos letras]:", data['continentCode'])
    if data['country'] == False:
     print('[~] [Código de continente de dos letras no encontrado!]')
  #---Latitud----##
    print("[~] [Latitud]:", data['lat'])
    if data['lat'] == False:
     print('[~] [Latitud no encontrada!]')
  ##----------Longitud------##
    print("[~] [Longitud]:", data['lon'])
    if data['lon'] == False:
      print('[~] [Longitud no encontrada!]')
  ##--------------Timezone---------##
    print("[~] [Zona horaria]:", data['timezone'])
    if data['timezone'] == False:
      print('[~] [Zona horaria no encontrada!]')
  ##-------------- ZIP--------------##
    print("[~] [Codigo zip]:", data['zip'])
    if data['zip'] == False:
      print('[~] [Codigo zip no encontrado!]')
  ##------------ AS -------------------##
    print("[~] [AS número y organización]:", data['as'])
    if data['as'] == False:
      print('[~] [AS número y organización no encontrado!]')
  ##-----------Countrycode-----##
    print("[~] [Código de país de dos letras]:", data['countryCode'])
    if data['countryCode'] == False:
     print('[~] [Código de país de dos letras no encontrado!]')
  ##-----------Reverse IP---------##
    print("[~] [DNS inverso de la IP]: ", data['reverse'])
    if data['reverse'] == False:
      print('[~] [DNS inverso de la IP!]')
  ##--------------Mobile------##
    print("[~] [Conexión móvil (celular)]:", data['mobile'])
    if data['mobile'] == False:
      print('[~] [Conexión móvil no encontrado!]')
  #----currency----##
    print('[~] [Moneda nacional]:', data['currency'])
    if data['currency'] == False:
      print('[~] [Moneda nacional no encontrada!]')
  #-----district----#
    print('[~] [Distrito (subdivisión de la city)]:', data['district'])
    if data['district'] == False:
      print('[~] [Distrito no encontrado!]')
  #-------Proxy-----#
    print('[~] [Proxy, VPN o Tor]:', data['proxy'])
    if data['proxy'] == False:
      print('[~] [Proxy, VPN o Tor no encontrado!]')
  except KeyError:
    print(f'\n[~] Error al intentar obtener datos de {ipin}')

def menu():
  print(logo)
  print('[1] TRACK ANY IP')
  print('[2] SHOW MY DETAILS IP')
  print('[99] EXIT')
  var = int(input('\n>> '))
  if var == 1:
    locate()
  elif var == 2:
    per()
  elif var == 99:
    print('\n[~] Saliendo del programa...')
    time.sleep(1)
    exit()
  else:
    print('\n[~] Error opcion invalida.')
    time.sleep(2)
    menu()

menu()
